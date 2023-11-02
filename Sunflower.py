import pygame

class Sunflower(pygame.sprite.Sprite):
    def __init__(self,lasttime):
        super(Sunflower,self).__init__()
        self.image = pygame.image.load('material/images/SunFlower_00.png').convert_alpha()
        self.images = [pygame.image.load('material/images/SunFlower_{:02d}.png'.format(i)).convert_alpha() for i in range(0,13)]
        self.rect = self.images[0].get_rect()
        self.lasttime = lasttime
        self.energy = 200
        self.zombies = set()


    def update(self, *args):
        for zombie in self.zombies:
            if not zombie.isAlive:
                continue
            self.energy -= 1
            if self.energy <= 0:
                for zombie in self.zombies:
                    zombie.isMeet = False
                self.kill()
        self.image = self.images[args[0] % len(self.images)]