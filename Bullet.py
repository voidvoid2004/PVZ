import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self,pearect,screensize):
        super(Bullet,self).__init__()
        self.image = pygame.image.load('material/images/Bullet_1.png').convert_alpha()
        self.rect = self.image.get_rect()


        self.rect.top = pearect[1]
        self.rect.left = pearect[0] + 45
        self.width = screensize[0]
        self.speed = 20


    def update(self, *args):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.kill()

