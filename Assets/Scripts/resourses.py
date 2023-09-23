import pygame

# Завантаження гравця
player_texture = pygame.image.load('../Images/Player/character_0000.png')
player_image = pygame.transform.flip(pygame.transform.scale(player_texture, (42, 42)), True, False)

# Завантаження тайлів
tile_size = 36
background_image = pygame.transform.scale(
    pygame.image.load('../Images/Tiles/Backgrounds/background_0000.png'),
    (tile_size, tile_size))  # Tile - 1
background_image_2 = pygame.transform.scale(
    pygame.image.load('../Images/Tiles/Backgrounds/background_0001.png'),
    (tile_size, tile_size))  # Tile - 2
background_image_3 = pygame.transform.scale(
    pygame.image.load('../Images/Tiles/Backgrounds/background_0002.png'),
    (tile_size, tile_size))  # Tile - 3
grass_image = pygame.transform.scale(
    pygame.image.load('../Images/Tiles/Grass/tile_0000.png'),
    (tile_size, tile_size))  # Tile - 4
grass_image_2 = pygame.transform.scale(
    pygame.image.load('../Images/Tiles/Grass/tile_0002.png'),
    (tile_size, tile_size))  # Tile - 5
grass_image_3 = pygame.transform.scale(
    pygame.image.load('../Images/Tiles/Grass/tile_0003.png'),
    (tile_size, tile_size))  # Tile - 6
grass_image_4 = pygame.transform.scale(
    pygame.image.load('../Images/Tiles/Grass/tile_0004.png'),
    (tile_size, tile_size))  # Tile - 7
block = pygame.transform.flip(pygame.transform.scale(
    pygame.image.load('../Images/Tiles/Blocks/tile_0009.png'),
    (tile_size, tile_size)), True, False)  # Tile - 8
block_2 = pygame.transform.scale(
    pygame.image.load('../Images/Tiles/Blocks/tile_0009.png'),
    (tile_size, tile_size))  # Tile - 9

# Створення словника для збереження відповідності між номерами типів тайлів та їх зображенням
tile_images = {
    1: background_image,
    2: background_image_2,
    3: background_image_3,
    4: grass_image,
    5: grass_image_2,
    6: grass_image_3,
    7: grass_image_4,
    8: block,
    9: block_2
}
