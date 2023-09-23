import pygame

# Завантаження гравця
player_texture = pygame.image.load('../Images/Player/character_0000.png')
player_image = pygame.transform.flip(pygame.transform.scale(player_texture, (42, 42)), True, False)

# Завантаження тайлів
tile_size = 36
background_image_0 = pygame.transform.scale(
    pygame.image.load('../Images/Tiles/Backgrounds/background_0000.png'),
    (tile_size, tile_size))  # Tile - 1
background_image_1 = pygame.transform.scale(
    pygame.image.load('../Images/Tiles/Backgrounds/background_0001.png'),
    (tile_size, tile_size))  # Tile - 2
background_image_2 = pygame.transform.scale(
    pygame.image.load('../Images/Tiles/Backgrounds/background_0002.png'),
    (tile_size, tile_size))  # Tile - 3

grass_image_0 = pygame.transform.scale(
    pygame.image.load('../Images/Tiles/Grass/tile_0000.png'),
    (tile_size, tile_size))  # Tile - 4
grass_image_1 = pygame.transform.scale(
    pygame.image.load('../Images/Tiles/Grass/tile_0001.png'),
    (tile_size, tile_size))  # Tile - 5
grass_image_2 = pygame.transform.scale(
    pygame.image.load('../Images/Tiles/Grass/tile_0002.png'),
    (tile_size, tile_size))  # Tile - 6
grass_image_3 = pygame.transform.scale(
    pygame.image.load('../Images/Tiles/Grass/tile_0003.png'),
    (tile_size, tile_size))  # Tile - 7
grass_image_4 = pygame.transform.scale(
    pygame.image.load('../Images/Tiles/Grass/tile_0004.png'),
    (tile_size, tile_size))  # Tile - 8

block_0 = pygame.transform.flip(pygame.transform.scale(
    pygame.image.load('../Images/Tiles/Blocks/tile_0009.png'),
    (tile_size, tile_size)), True, False)  # Tile - 9
block_1 = pygame.transform.scale(
    pygame.image.load('../Images/Tiles/Blocks/tile_0009.png'),
    (tile_size, tile_size))  # Tile - 10
block_2 = pygame.transform.scale(
    pygame.image.load('../Images/Tiles/Blocks/tile_0011.png'),
    (tile_size, tile_size))  # Tile - 11

# Створення словника для збереження відповідності між номерами типів тайлів та їх зображенням
tile_images = {
    1: background_image_0,
    2: background_image_1,
    3: background_image_2,
    4: grass_image_0,
    5: grass_image_1,
    6: grass_image_2,
    7: grass_image_3,
    8: grass_image_4,
    9: block_0,
    10: block_1,
    11: block_2
}
