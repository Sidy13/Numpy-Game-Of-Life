import pygame


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Game of life")
        self.keep = True
        self.grid = Grid(self.screen)

        # self.square =

    def run(self):
        left = 1
        right = 3
        while self.keep:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.keep = False
                elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    self.grid.update_cell()
            self.grid.update_grid()
            self.screen.fill((240, 240, 240))
            self.grid.print()
            pygame.display.update()
            pygame.display.flip()


class Grid:
    def __init__(self, screen):
        self.screen = screen
        self.grid_size = 50
        self.cell_size = 600 // self.grid_size
        self.grid = [[0] * self.grid_size for _ in range(self.grid_size)]

    def print(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j] == 1:
                    self.black_square(i, j)
                else:
                    self.white_square(i, j)

        for i in range(self.grid_size + 1):
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * self.cell_size), (600, i * self.cell_size))
        for j in range(self.grid_size + 1):
            pygame.draw.line(self.screen, (0, 0, 0), (j * self.cell_size, 0), (j * self.cell_size, 600))


    def black_square(self, i, j):
        color = (0, 0, 0)
        pygame.draw.rect(self.screen, color, (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))
    def white_square(self, i ,j ):
        color = (255, 255, 255)
        pygame.draw.rect(self.screen, color, (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))


    def update_cell(self):
        position = pygame.mouse.get_pos()
        px, py = position[0] // self.cell_size, position[1] // self.cell_size
        self.grid[py][px] = 1

    def count_neighbors(self, i, j):
        count = 0

        # Parcourir les positions des voisins potentiels
        for x in range(-1, 2):
            for y in range(-1, 2):
                # Ignorer la cellule elle-même
                if x == 0 and y == 0:
                    continue

                # Calculer les coordonnées du voisin
                neighbor_x, neighbor_y = i + x, j + y

                # Vérifier si le voisin est à l'intérieur de la grille
                if 0 <= neighbor_x < self.grid_size and 0 <= neighbor_y < self.grid_size:
                    # Incrémenter le compteur si le voisin est vivant
                    count += self.grid[neighbor_x][neighbor_y]

        return count

    def update_grid(self):
        new_grid = [[0] * self.grid_size for _ in range(self.grid_size)]

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j] == 1:
                    new_grid[i][j] = 1
                    continue

                neighbors = self.count_neighbors(i, j)
                if self.grid[i][j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_grid[i][j] = 0
                        self.white_square(i,j)
                    else:
                        new_grid[i][j] = 1
                        self.black_square(i, j)
                else:
                    if neighbors == 3:
                        new_grid[i][j] = 1
                        self.black_square(i, j)
                    else:
                        self.white_square(i,j)

        self.grid = new_grid
