import pygame
import random

pygame.init()

# экран
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# игрок
player_x = WIDTH // 2
player_y = HEIGHT - 100
player_speed = 7

# враг
enemy_x = random.randint(50, WIDTH - 50)
enemy_y = -100
enemy_speed = 5

# монеты
coins = []
coin_timer = 0
score = 0

font = pygame.font.SysFont("Arial", 24)

class Coin:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = -20
        self.weight = random.choice([1, 2, 3])  # разный вес

    def move(self):
        self.y += 5

    def draw(self):
        color = (255, 215, 0)
        pygame.draw.circle(screen, color, (self.x, self.y), 10)

running = True

while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # спавн монет
    coin_timer += 1
    if coin_timer > 60:
        coins.append(Coin())
        coin_timer = 0

    # монеты
    for coin in coins[:]:
        coin.move()
        coin.draw()

        # сбор
        if abs(coin.x - player_x) < 30 and abs(coin.y - player_y) < 30:
            score += coin.weight
            coins.remove(coin)

    # ускорение врага
    enemy_y += enemy_speed + score // 5

    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(50, WIDTH - 50)

    # отрисовка игрока и врага
    pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, 40, 40))
    pygame.draw.rect(screen, (255, 0, 0), (enemy_x, enemy_y, 40, 40))

    # счёт
    text = font.render(f"Coins: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()