import pygame
import random

BLOCK_SIZE = 20
MAP_SIZE = [800, 500]


class Apple(pygame.sprite.Sprite):
    def __init__(self, fullSnake):
        pygame.sprite.Sprite.__init__(self)
        while True:
            self.location = [random.randint(0, MAP_SIZE[0] // BLOCK_SIZE - 1),
                             random.randint(0, MAP_SIZE[1] // BLOCK_SIZE - 1)]
            if self.location not in fullSnake:
                break
        self.color = (255, 0, 0)

    # 定义Apple对象的动作
    def draw(self, screen):
        cx, cy = int((self.location[0] + 0.5) * BLOCK_SIZE), int((self.location[1] + 0.5) * BLOCK_SIZE)
        pygame.draw.circle(screen, self.color, (cx, cy), BLOCK_SIZE // 2 - 2)
