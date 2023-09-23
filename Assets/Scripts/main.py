import pygame
from resourses import player_image, tile_images
from character import Character
from map import tile_map
from font import font, text_surface, start_time

# Ініціалізація pygame
pygame.init()

# Задання розміру екрана
SCREEN_WIDTH = 935
SCREEN_HEIGHT = 500

# Встановлення розміру екрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Встановлення назви гри
pygame.display.set_caption('Smurf Adventures / Смурфік: Пригоди')

# Встановлення значка гри
icon = pygame.image.load('../../icon.png')
pygame.display.set_icon(icon)

# Створення таймера
clock = pygame.time.Clock()

# Змінні, що відповідають за параметри карти
map_width = len(tile_map[0])
map_height = len(tile_map)
tile_size = 36

# Початкове зміщення карти
shift_x = 0
shift_y = 0


# Функція для малювання карти
def draw_map():
    screen.fill((223, 246, 245))
    for y in range(map_height):
        for x in range(map_width):
            tile_type = tile_map[y][x]
            tile_x = x * tile_size
            tile_y = y * tile_size
            tile_rect = pygame.Rect(tile_x + shift_x, tile_y + shift_y, tile_size, tile_size)

            # Використання словника для вибору зображення тайлу
            if tile_type in tile_images:
                screen.blit(tile_images[tile_type], tile_rect)


# Створення списку землі
ground_list = [pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size) for y in range(map_height)
               for x in range(map_width) if tile_map[y][x] in [5, 6, 8, 9]]


# Функція для відмалювання контурів карти
def draw_line(draw):
    if draw:
        for line in range(0, 26):
            pygame.draw.line(screen, (0, 0, 0), (0, line * tile_size), (SCREEN_WIDTH, line * tile_size))
            pygame.draw.line(screen, (0, 0, 0), (line * tile_size, 0), (line * tile_size, SCREEN_HEIGHT))
    else:
        pass


# Параметри для гравітації
gravity = 0.1
on_ground = False
player_velocity_y = 0

# Створення гравця
player = Character(player_image, 90, 200)

# Параметри гравця
player_direction = 1  # 1 - праворуч, -1 - ліворуч

# Основний цикл гри
respawn = False
start = True
while start:

    # Перевірка подій
    for event in pygame.event.get():
        # Якщо це закриття вікна
        if event.type == pygame.QUIT:
            start = False  # Закрити вікно

    # Зміщення карти
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_direction = - 1
        shift_x += 5
        for tile in ground_list:
            tile.x += 5
    elif keys[pygame.K_d]:
        player_direction = 1
        shift_x -= 5
        for tile in ground_list:
            tile.x -= 5

    # Гравітація
    if not on_ground:
        player_velocity_y += gravity
    else:
        player_velocity_y = 0

    player.rect.y += player_velocity_y

    # Колізія між гравцем та землею
    on_ground = False
    for tile_rect in ground_list:
        if (player.rect.colliderect(
                tile_rect) and player.rect.y + player.rect.height <= tile_rect.y + player_velocity_y + 5.35
                and not (player.rect.y > tile_rect.y + player_velocity_y)):
            on_ground = True
            player.rect.y = tile_rect.y - player.rect.height

    # Перевірка виходу поза карту
    if player.rect.y >= 500:
        for tile in ground_list:
            tile.x -= shift_x
        # Встановлення початкових значень карти
        shift_x = 0
        shift_y = 0

        # Встановлення початкових значень гравця
        player.rect.y = 200
        player_velocity_y = 0

        respawn = True

    keys = pygame.key.get_pressed()
    if on_ground:
        player_velocity_y = 0
        if keys[pygame.K_w]:
            player_velocity_y -= 5.35
            on_ground = False

    # Малювання карти та гравця
    draw_map()
    player.draw(screen, False)
    draw_line(False)

    # Відображаємо гравця з відзеркаленням
    if player_direction == 1:
        screen.blit(player_image, player.rect)
    else:
        flipped_player = pygame.transform.flip(player_image, True, False)
        screen.blit(flipped_player, player.rect)


    if respawn:
        # Перевірка, чи минуло 3 секунди
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 4000:
            text_surface = font.render('', True, (0, 0, 0))  # Змінюємо текст на порожній рядок

        # Виведення тексту на екран
        screen.blit(text_surface, (0, 0))
    # Обмеження частоти кадрів за секунду
    clock.tick(60)

    # Оновлення екрану
    pygame.display.update()
pygame.quit()
