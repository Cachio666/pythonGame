# 运行主函数
import sys
from modules import *

BLOCK_SIZE = 20
MAP_SIZE = [800, 500]
FPS = 5
BLACK = [0, 0, 0]


def main():
    # 游戏初始化
    pygame.init()
    screen = pygame.display.set_mode(MAP_SIZE)  # 设置游戏屏幕地图的大小
    pygame.display.set_caption("Cachio的贪吃蛇游戏")
    clock = pygame.time.Clock()

    # 选择背景音乐
    # pygame.mixer.music.load()  # 这里要选择音乐文件
    # pygame.mixer.music.play(-1)

    # 游戏主循环
    """
    实例化 snake 和 food 的对象
    循环更新游戏 screen 的状态
    """
    snake = Snake()
    food = Apple(snake.fullSnake)
    score = 0
    while True:
        screen.fill(BLACK)
        # 按键检测
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    # 设置方向
                    snake.changeDirect({pygame.K_UP: 'up', pygame.K_DOWN: 'down', pygame.K_LEFT: 'left', pygame.K_RIGHT: 'right'}[event.key])

        # 更新snake和food
        if snake.update(food):
            food = Apple(snake.fullSnake)
            score += 1

        # 判断游戏是否结束
        if snake.isGameOver():
            break

        # 更新游戏地图信息
        drawGameMap(screen)
        snake.draw(screen)
        food.draw(screen)
        showScore(score, screen)

        # 刷新地图
        pygame.display.update()
        clock.tick(FPS)

    return


if __name__ == '__main__':
    main()
