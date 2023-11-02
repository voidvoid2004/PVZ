import pygame
import random

class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super(Zombie,self).__init__()
        self.image = pygame.image.load('material/images/Zombie_0.png').convert_alpha()
        self.images = [pygame.image.load('material/images/Zombie_{}.png'.format(i)).convert_alpha() for i in range(0,22)]
        self.dieimage = [pygame.image.load('material/images/ZombieDie_{}.png'.format(i)).convert_alpha() for i in range(0,10)]
        self.attack_img = [pygame.image.load('material/images/ZombieAttack_{}.png'.format(i)).convert_alpha() for i in range(0,21)]
        self.rect = self.images[0].get_rect()
        self.rect.top = random.choice((55,155,292,420,525))
        self.rect.left = 1300
        self.speed = 1
        self.energy = 6
        self.dietime = 0
        self.isMeet = False
        self.isAlive = True


    def update(self, *args):
        if self.energy > 0:
            if self.isMeet:
                self.image = self.attack_img[args[0] % len(self.attack_img)]
            else:
                self.image = self.images[args[0] % len(self.images)]
            if not self.isMeet:
                self.rect.left -= self.speed
        else:
            self.isAlive = False
            if self.dietime < 20:
                self.image = self.dieimage[self.dietime//2]
                self.dietime += 1
            else:
                if self.dietime > 30:
                    self.kill()
                else:
                    self.dietime += 1
