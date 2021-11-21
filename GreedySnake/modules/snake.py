import copy
import random
import pygame

BLOCK_SIZE = 20
MAP_SIZE = [800, 500]


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.head = [random.randint(5, 10), random.randint(5, 10)]
        self.body = []
        for i in range(1, 3):
            self.body.append([self.head[0], self.head[1] - 1])
        self.direction = 'right'
        self.head_colors = [(0, 80, 255), (0, 255, 255)]
        self.body_colors = [(0, 155, 0), (0, 255, 0)]

    # 定义蛇对象的动作
    def changeDirect(self, direction):
        assert direction in ['up', 'down', 'left', 'right']
        if self.direction != direction:
            self.direction = direction

    def draw(self, screen):
        head_x, head_y = self.head[0] * BLOCK_SIZE, self.head[1] * BLOCK_SIZE
        rect = pygame.Rect(head_x, head_y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, self.head_colors[0], rect)
        rect = pygame.Rect(head_x - 4, head_y - 4, BLOCK_SIZE - 8, BLOCK_SIZE - 8)
        pygame.draw.rect(screen, self.head_colors[1], rect)

        for ele in self.body:
            body_x, body_y = ele[0] * BLOCK_SIZE, ele[1] * BLOCK_SIZE
            rect = pygame.Rect(body_x, body_y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, self.body_colors[0], rect)
            rect = pygame.Rect(body_x - 4, body_y - 4, BLOCK_SIZE - 8, BLOCK_SIZE - 8)
            pygame.draw.rect(screen, self.body_colors[1], rect)

    def isGameOver(self):
        # 出界，吃到自己
        length = MAP_SIZE[0] // BLOCK_SIZE
        width = MAP_SIZE[1] // BLOCK_SIZE
        if self.head[0] < 0 or self.head[1] < 0 or self.head[0] > length or self.head[1] > width:
            return True
        if self.head in self.body:
            return True
        return False

    def update(self, food):
        self.body.insert(0, copy.deepcopy(self.head))
        if self.direction == 'up':
            self.head[1] -= 1
        elif self.direction == 'down':
            self.head[1] += 1
        elif self.direction == 'left':
            self.head[0] -= 1
        elif self.direction == 'right':
            self.head[0] += 1

        if self.head == food.location:
            return True
        else:
            self.body = self.body[:-1]
            return False

    @property
    def fullSnake(self):
        return [self.head] + self.body
