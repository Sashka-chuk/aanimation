import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка параметров экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Комета")

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Определение параметров кометы
comet_vertices = [(0, 0), (10, -5), (5, 5), (0, 5), (0, 0)]

# Переменные для перемещения кометы
comet_x = WIDTH
comet_y = 0
speed_x = -0.1
speed_y = 0.1
speed_multiplier = 1


class Rocket1:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = 0
        self.height = 0
        self.color = (255, 255, 255)
        self.vertices = [(30, 0), (20, 10), (-30, 10), (-40, 20), (-60, 20), (-50, 10), (-50, -10), (-60, -20),
                         (-40, -20), (-30, -10),
                         (20, -10)]
        self.x = self.width
        self.y = 100
        self.speed_x = 0.1
        self.speed_y = 0.1

    def draw(self):
        pygame.draw.polygon(self.screen, self.color, [(self.x + vx, self.y + vy) for vx, vy in self.vertices])

    def update(self):
        self.x += self.speed_x * speed_multiplier
        if self.x < 0:
            self.x = self.width


rocket = Rocket1(screen, WIDTH, HEIGHT)

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill(BLACK)

    # Рисование кометы
    pygame.draw.polygon(screen, WHITE, [(comet_x + vx, comet_y + vy) for vx, vy in comet_vertices])

    # Перемещение кометы
    comet_x += speed_x
    comet_y += speed_y
    rocket.draw()
    rocket.update()
    # Если комета вышла за пределы экрана, переместить ее в правый верхний угол
    if comet_x < 0 or comet_y > HEIGHT:
        comet_x = WIDTH
        comet_y = 0

    # Обновление экрана
    pygame.display.flip()

    # Задержка для плавной анимации
    pygame.time.delay(10)

# Выход из Pygame
pygame.quit()
sys.exit()
