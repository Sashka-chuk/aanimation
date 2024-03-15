import pygame
import sys
import math
import random

# Инициализация Pygame
pygame.init()

# Установка параметров экрана
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Солнечная система")

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
mercuryColor = (214, 180, 58)
venusColor = (236, 214, 126)
earthColor = (2, 101, 250)
marsColor = (237, 61, 7)
jupiterColor = (242, 109, 0)


# Класс для представления планет
class Planet:
    def __init__(self, color, distance, radius, speed):
        self.color = color
        self.distance = distance
        self.radius = radius
        self.speed = speed
        self.angle = 0

    def draw(self):
        x = WIDTH // 2 + self.distance * math.cos(math.radians(self.angle))
        y = HEIGHT // 2 + self.distance * math.sin(math.radians(self.angle))
        pygame.draw.circle(screen, self.color, (int(x), int(y)), self.radius)

    def update(self):
        self.angle += self.speed * speed_multiplier


# Класс для представления спутников
class Satellite:
    def __init__(self, parent_planet, color, distance, radius, speed):
        self.parent_planet = parent_planet
        self.color = color
        self.distance = distance
        self.radius = radius
        self.speed = speed
        self.angle = 0

    def draw(self):
        parent_x = WIDTH // 2 + self.parent_planet.distance * math.cos(math.radians(self.parent_planet.angle))
        parent_y = HEIGHT // 2 + self.parent_planet.distance * math.sin(math.radians(self.parent_planet.angle))
        x = parent_x + self.distance * math.cos(math.radians(self.angle))
        y = parent_y + self.distance * math.sin(math.radians(self.angle))
        pygame.draw.circle(screen, self.color, (int(x), int(y)), self.radius)

    def update(self):
        self.angle += self.speed * speed_multiplier


# Определение параметров точек
point_radius = 1
points = []


def create_point():
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    return (x, y)


# Создание объектов для планет
sun = Planet(YELLOW, 0, 30, 0)
mercury = Planet(mercuryColor, 80, 5, 1)
venus = Planet(venusColor, 120, 10, 0.8)
earth = Planet(earthColor, 180, 12, 0.6)
mars = Planet(marsColor, 240, 8, 0.5)
jupiter = Planet(jupiterColor, 300, 20, 0.4)
planets = [mercury, venus, earth, mars, jupiter]

# Создание спутника для Земли
moon = Satellite(earth, WHITE, 30, 3, 1.5)
earth.satellites = [moon]  # Список спутников Земли

# Переменная для регулировки скорости анимации
speed_multiplier = 1.0

f1 = pygame.font.Font(None, 36)

# Основной цикл программы
running = True
while running:
    # Добавление новой точки
    if len(points) < 150:  # Ограничение числа точек для оптимизации
        points.append(create_point())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed_multiplier += 0.5
                pygame.display.update()
            elif event.key == pygame.K_DOWN:
                speed_multiplier -= 0.5
                pygame.display.update()
                # if speed_multiplier < 0: # граница
                #     speed_multiplier = 0

    # Очистка экрана
    screen.fill(BLACK)

    # Создание звездочек
    for point in points:
        pygame.draw.circle(screen, WHITE, point, point_radius)

    # Рисование и обновление планет
    for planet in planets:
        text1 = f1.render(f"{'%.1f' % speed_multiplier}", True,
                          (250, 250, 250))
        screen.blit(text1, (10, 50))
        planet.draw()
        planet.update()

        # Обновление и рисование спутников
        if hasattr(planet, 'satellites'):
            for satellite in planet.satellites:
                satellite.draw()
                satellite.update()

    sun.draw()
    # Переключение буферов
    pygame.display.flip()

    # Задержка для плавной анимации
    pygame.time.delay(10)

# Выход из Pygame
pygame.quit()
sys.exit()
