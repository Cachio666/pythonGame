import pygame
import sys

BLOCK_SIZE = 20
MAP_SIZE = [800, 500]


def endInterface(screen):
    font_size_big = 60
    font_size_small = 30
    font_color = (255, 255, 255)
    font_big = pygame.font.Font("arial", font_size_big)
    font_small = pygame.font.Font("arial", font_size_small)
    surface = screen.convert_alpha()
    surface.fill((0, 0, 0, 5))
    text = font_big.render('Game Over!', True, font_color)
    text_rect = text.get_rect()
    text_rect.centerx, text_rect.centery = MAP_SIZE[0]//2, MAP_SIZE[1]//2-50
    surface.blit(text, text_rect)
    button_width, button_height = 100, 40
    button_start_x_left = MAP_SIZE[0] // 2 - button_width - 20
    button_start_x_right = MAP_SIZE[0] // 2 + 20
    button_start_y = MAP_SIZE[1] // 2 - button_height // 2 + 20
    pygame.draw.rect(surface, (128, 128, 128), (button_start_x_left, button_start_y, button_width, button_height))
    text_restart = font_small.render('Restart', True, font_color)
    text_restart_rect = text_restart.get_rect()
    text_restart_rect.centerx, text_restart_rect.centery = button_start_x_left + button_width / 2, button_start_y + button_height / 2
    surface.blit(text_restart, text_restart_rect)
    pygame.draw.rect(surface, (128, 128, 128), (button_start_x_right, button_start_y, button_width, button_height))
    text_quit = font_small.render('Quit', True, font_color)
    text_quit_rect = text_quit.get_rect()
    text_quit_rect.centerx, text_quit_rect.centery = button_start_x_right + button_width / 2, button_start_y + button_height / 2
    surface.blit(text_quit, text_quit_rect)
    while True:
        screen.blit(surface, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button:
                if text_quit_rect.collidepoint(pygame.mouse.get_pos()):
                    return False
                if text_restart_rect.collidepoint(pygame.mouse.get_pos()):
                    return True
        pygame.display.update()