import pygame

BLOCK_SIZE = 20
MAP_SIZE = [800, 500]


def drawGameMap(screen):
    color = [40, 40, 40]
    for x in range (0, MAP_SIZE[0], BLOCK_SIZE):
        pygame.draw.line(screen, color, (x, 0), (x, MAP_SIZE[1]))
    for y in range (0, MAP_SIZE[1], BLOCK_SIZE):
        pygame.draw.line(screen, color, [0, y], [MAP_SIZE[0], y])


def showScore(score, screen):
    color = [255, 255, 255]
    font = pygame.font.SysFont("arial", 30)
    text = font.render('Score: %s' % score, True, color)
    rect = text.get_rect()
    rect.topleft = (10, 10)
    screen.blit(text, rect)