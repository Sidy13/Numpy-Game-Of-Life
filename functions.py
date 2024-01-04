import time
import pygame
import numpy as np

BG_COLOR = (10,10,10)
GRID_COLOR = (40,40,40)
DIE_NEXT_COLOR = (170,170,170)
ALIVE_NEXT_COLOR = (255,255,255)

def update(screen, cells, size, with_progress = False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row,col in np.ndindex(cells.shape):
        alive = np.sum(cells[(row - 1):(row + 2), (col - 1):(col + 2)]) - cells[row, col]
        alive = max(0, alive)
        color = BG_COLOR if cells[row,col] == 0 else ALIVE_NEXT_COLOR

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = DIE_NEXT_COLOR
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = ALIVE_NEXT_COLOR
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = ALIVE_NEXT_COLOR

        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return updated_cells

def running():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    cells = np.zeros((60, 80))
    screen.fill(GRID_COLOR)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    run = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = not run
                    update(screen, cells, 10)
                    pygame.display.update()
            elif pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10)
                pygame.display.update()

        screen.fill(GRID_COLOR)

        if run:
            cells = update(screen, cells, 10, with_progress=True)
            pygame.display.update()
            time.sleep(0.5)



