import pygame


class Character:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = x, y

    def draw(self, screen, draw_hitbox):
        if draw_hitbox:
            pygame.draw.rect(screen, (0, 255, 0), (self.rect.x, self.rect.y, 42, 42))
        screen.blit(self.image, (self.rect.x, self.rect.y))
