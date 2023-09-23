import pygame

pygame.init()

# Шрифт для виводу тексту
font = pygame.font.Font('../Fonts/NunitoSans_7pt-SemiBoldItalic.ttf', 24)

# Створення текстової поверхні з текстом
text_surface = font.render('*Respawn', True, (0, 0, 0))

# Початковий час відображення тексту
start_time = pygame.time.get_ticks()
