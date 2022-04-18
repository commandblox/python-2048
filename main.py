import sys
import numpy as np
import pygame

w, h = size = 500, 500
game_size = 4
block_size = w / game_size
block_border_size = 5

font = pygame.font.Font("arial.ttf", 16)


class Board:
    def __init__(self):
        self.blocks = np.zeros((game_size, game_size), int)

    def show(self):
        for x in range(game_size):
            for y in range(game_size):
                block = self.blocks[x, y]
                rect0 = [x * block_size + (block_border_size / 2), y * block_size + (block_border_size / 2),
                         block_size - block_border_size, block_size - block_border_size]
                rect1 = [x * block_size, y * block_size, block_size, block_size]

                pygame.draw.rect(screen, (100, 100, 100), rect1)
                pygame.draw.rect(screen, (255, 255, 255), rect0)

                if block:
                    text = font.render(str(block), False)
                    text_rect = text.get_rect()
                    text_rect.center = (x+block_size/2, y+block_size/2)


if __name__ == '__main__':
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("2048", "2048")
    board = Board()
    while 1:
        screen.fill((0, 0, 0))
        board.show()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
