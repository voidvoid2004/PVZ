import pygame
import sys
import time
import random
from Peashooter import Peashooter
from Sunflower import Sunflower
from Wallnut import Wallnut
from Sun import Sun
from Zombie import Zombie
from Bullet import Bullet
from FlagZombie import FlagZombie
from NatureSun import NatureSun

pygame.init()
big_size = (1300, 700)
screen = pygame.display.set_mode((1300, 700))
pygame.display.set_caption('植物大战僵尸')

pygame.mixer.init()
pygame.mixer.music.load("material/music/18 - Crazy Dave IN-GAME.mp3")

background_image_path = "material/images/background1.jpg"
sunback_image_path = 'material/images/SunBack.png'
background = pygame.image.load(background_image_path).convert()
sunback = pygame.image.load(sunback_image_path).convert()
seedbackimg = pygame.image.load('material/images/SeedBank.png')
flower_seed = pygame.image.load('material/images/Sunflower.gif')
wallnut_seed = pygame.image.load('material/images/WallNut.gif')
peashooter_seed = pygame.image.load('material/images/Peashooter.gif')
sunflowerimg = pygame.image.load('material/images/SunFlower_00.png').convert_alpha()
peashooterimg = pygame.image.load('material/images/Peashooter_00.png').convert_alpha()
wallnutimg = pygame.image.load('material/images/Wallnut_00.png').convert_alpha()
game_surface = pygame.image.load('material/images/Surface.png').convert()
button1 = pygame.image.load('material/images/1.png').convert_alpha()
button2 = pygame.image.load('material/images/2.png').convert_alpha()
failm = pygame.image.load('material/images/GameOver.png').convert()
logo = pygame.image.load('material/images/logo.jpg').convert_alpha()

pygame.display.set_icon(logo)

text = '150'
suns_font = pygame.font.SysFont('arial', 20)
suns_number_surface = suns_font.render(text, True, (0, 0, 0))


sunflowergroup = pygame.sprite.Group()
sunList = pygame.sprite.Group()
bulletgroup = pygame.sprite.Group()
zombiegroup = pygame.sprite.Group()
wallnutgroup = pygame.sprite.Group()
peashootergroup = pygame.sprite.Group()


GEN_SUN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(GEN_SUN_EVENT, random.randint(5000, 7000))

GEN_BULLET_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(GEN_BULLET_EVENT, 1000)

GEN_ZOMBIE_EVENT = pygame.USEREVENT + 3
pygame.time.set_timer(GEN_ZOMBIE_EVENT, random.randint(7000, 20000))

GEN_FLAGZOMBIE_EVENT = pygame.USEREVENT + 4
pygame.time.set_timer(GEN_FLAGZOMBIE_EVENT, random.randint(9000, 20000))

GEN_NATURESUN_EVENT = pygame.USEREVENT + 5
pygame.time.set_timer(GEN_NATURESUN_EVENT, 7000)

choose = 0

win = True


def main():
    global text
    global suns_number_surface
    global suns_font
    global choose
    global win
    index = 0
    clock = pygame.time.Clock()
    gamelist = True
    while gamelist:
        clock.tick(30)
        buttons = pygame.mouse.get_pressed()
        x1,y1 = pygame.mouse.get_pos()
        if 1150 <= x1 <=1260 and 575 <= y1 <= 690 and buttons[0]:
            sys.exit()
        if 750<=x1<1080 and 150<=y1<=270:
            screen.blit(button1,(750,150))
            if buttons[0]:
                gamelist = False
        else:
            screen.blit(game_surface,(0,0))
            screen.blit(button2,(750,150))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    Running = True
    while Running:


        if index >= 130:
            index = 0

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
        clock.tick(20)

        for bullet in bulletgroup:
            for zombie in zombiegroup:
                if pygame.sprite.collide_mask(bullet, zombie):
                    zombie.energy -= 1
                    bulletgroup.remove(bullet)

        for wallnut in wallnutgroup:
            for zombie in zombiegroup:
                if pygame.sprite.collide_mask(wallnut, zombie):
                    zombie.isMeet = True
                    wallnut.zombies.add(zombie)

        for peashooter in peashootergroup:
            for zombie in zombiegroup:
                if pygame.sprite.collide_mask(peashooter, zombie):
                    zombie.isMeet = True
                    peashooter.zombies.add(zombie)

        for sunflower in sunflowergroup:
            for zombie in zombiegroup:
                if pygame.sprite.collide_mask(sunflower, zombie):
                    zombie.isMeet = True
                    sunflower.zombies.add(zombie)
        for zombie in zombiegroup:
            if zombie.rect.left<165:
                win = False

        screen.blit(background, (0, 0))
        screen.blit(seedbackimg, (250, 0))
        screen.blit(suns_number_surface, (277, 58))
        screen.blit(flower_seed, (330, 8))
        screen.blit(peashooter_seed, (380, 8))
        screen.blit(wallnut_seed, (430, 8))
        if not win:
            screen.blit(failm, (400, 100))
            pygame.display.update()
            time.sleep(5)
            sys.exit()


        sunflowergroup.update(index)
        sunflowergroup.draw(screen)
        bulletgroup.update(index)
        bulletgroup.draw(screen)
        zombiegroup.update(index)
        zombiegroup.draw(screen)
        wallnutgroup.update(index)
        wallnutgroup.draw(screen)
        peashootergroup.update(index)
        peashootergroup.draw(screen)
        sunList.update(index)
        sunList.draw(screen)

        (x, y) = pygame.mouse.get_pos()

        if choose == 1:
            screen.blit(sunflowerimg, (x - 30, y - 30))

        elif choose == 2:
            screen.blit(peashooterimg, (x - 30, y - 30))

        elif choose == 3:
            screen.blit(wallnutimg, (x - 30, y - 30))

        index += 1

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == GEN_SUN_EVENT:
                for sprite in sunflowergroup:
                    now = time.time()
                    if now - sprite.lasttime >= random.randint(5, 15):
                        sun = Sun(sprite.rect)
                        sunList.add(sun)
                        sprite.lasttime = now

            if event.type == GEN_SUN_EVENT:
                xx = random.randint(300,1000)
                yy = random.randint(100,500)
                sun = NatureSun(xx,yy)
                sunList.add(sun)


            if event.type == GEN_BULLET_EVENT:
                for sprite in peashootergroup:
                    now = time.time()
                    if now - sprite.lasttime >= 2:
                        bullet = Bullet(sprite.rect, big_size)
                        bulletgroup.add(bullet)
                        sprite.lasttime = now

            if event.type == GEN_ZOMBIE_EVENT:
                zombie = Zombie()
                zombiegroup.add(zombie)

            if event.type == GEN_FLAGZOMBIE_EVENT:
                flagzombie = FlagZombie()
                zombiegroup.add(flagzombie)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed_key = pygame.mouse.get_pressed()

                if pressed_key[2]:
                    if choose == 1:
                        choose = 0
                    elif choose == 2:
                        choose = 0
                    elif choose == 3:
                        choose = 0

                elif pressed_key[0]:
                    pos = pygame.mouse.get_pos()
                    x, y = pos

                    if 330 <= x <= 380 and 8 <= y <= 78 and eval(text) >= 50:
                        choose = 1

                    elif 380 < x <= 430 and 8 <= y <= 78 and eval(text) >= 100:
                        choose = 2

                    elif 430 < x <= 480 and 8 <= y <= 78 and eval(text) >= 50:
                        choose = 3

                    elif 250 < x < 1150 and 70 < y < 700:

                        if choose == 1:
                            current_time = time.time()
                            sunflower = Sunflower(current_time)
                            sunflower.rect.center = (x, y)
                            sunflowergroup.add(sunflower)
                            choose = 0
                            text = str(eval(text) - 50)
                            suns_font = pygame.font.SysFont('arial', 20)
                            suns_number_surface = suns_font.render(text, True, (0, 0, 0))

                        elif choose == 2:
                            current_time = time.time()
                            peashooter = Peashooter(current_time)
                            peashooter.rect.center = (x, y)
                            peashootergroup.add(peashooter)
                            choose = 0
                            text = str(eval(text) - 100)
                            suns_font = pygame.font.SysFont('arial', 20)
                            suns_number_surface = suns_font.render(text, True, (0, 0, 0))

                        elif choose == 3:
                            wallnut = Wallnut()
                            wallnut.rect.center = (x, y)
                            wallnutgroup.add(wallnut)
                            choose = 0
                            text = str(eval(text) - 50)
                            suns_font = pygame.font.SysFont('arial', 20)
                            suns_number_surface = suns_font.render(text, True, (0, 0, 0))

                    else:
                        pass

                    for sun in sunList:
                        if sun.rect.collidepoint(pos):
                            sunList.remove(sun)
                            text = str(eval(text) + 25)
                            suns_font = pygame.font.SysFont('arial', 20)
                            suns_number_surface = suns_font.render(text, True, (0, 0, 0))

        pygame.display.update()



if __name__ == '__main__':
    main()

