import pygame
import random


class NatureSun(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super(NatureSun, self).__init__()

        self.image = pygame.image.load('material/images/Sun_1.png').convert_alpha()
        self.images = [pygame.image.load('material/images/Sun_{}.png'.format(i)).convert_alpha() for i in range(1, 18)]
        self.rect = self.images[0].get_rect()


        self.rect.top = y
        self.rect.left = x

    def update(self, *args):
        self.image = self.images[args[0] % len(self.images)]

