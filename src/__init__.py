import pygame
import sys

import time

from src.Boat import Boat
from src.Man import Man
from src.Monster import Monster

game_lose = False
game_win = False

pygame.init()

win = pygame.display.set_mode((1000, 700))

pygame.display.set_caption("Missinory and cannibal")

bg = pygame.image.load('images\\download.png')

mons = pygame.image.load('images\\reuk.png')
font = pygame.font.SysFont("Arial", 25)
font2 = pygame.font.SysFont("Arial", 20)
font1 = pygame.font.SysFont("Bold", 65)
text = font.render("Press Key A S D to move the missionary", True, (255, 255, 255))
text1 = font.render("Press Key F G H to move the cannibal", True, (255, 255, 255))
text2 = font.render("Press Key Space to move the boat", True, (255, 255, 255))
text3 = font1.render("You Lose", True, (255, 0, 0))
text4 = font1.render("You Won", True, (255, 0, 0))

clock = pygame.time.Clock()


def draw():
    win.blit(bg, (0, 0))

    man_one.draw(win)
    man_two.draw(win)
    man_three.draw(win)
    monster_one.draw(win)
    monster_two.draw(win)
    monster_three.draw(win)

    boat.draw_boat(win)
    win.blit(text, (20, 5))
    win.blit(text1, (20, 30))
    win.blit(text2, (20, 55))

    if game_lose:
        win.blit(text3, (430, 300))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                exit()

    if game_win:
        win.blit(text4, (430, 300))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                exit()

    pygame.display.update()


boat = Boat(330, 465, 100, 100)

man_one = Man(220, 420, 64, 64, 'man_one')
man_two = Man(200, 420, 64, 64, 'man_two')
man_three = Man(180, 420, 64, 64, 'man_three')
monster_one = Monster(160, 420, 64, 64, 'monster_one')
monster_two = Monster(140, 420, 64, 64, 'monster_two')
monster_three = Monster(120, 420, 64, 64, 'monster_three')

stop = 0
left = 1
right = 2
run = True


def move_left():
    global game_lose
    global game_win

    while True:
        state_left = font2.render('(' + str(Boat.left_man) + ',' + str(Boat.left_monster) + ',0)', True,
                                  (255, 255, 255))
        state_right = font2.render('(' + str(Boat.right_man) + ',' + str(Boat.right_monster) + ',1)', True,
                                   (255, 255, 255))
        win.blit(state_left, (900, 5))
        win.blit(state_right, (900, 30))
        pygame.display.update()

        draw()

        clock.tick(27)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_a:
                    if len(Boat.test) < 2 and (man_one.position == boat.position):
                        Boat.test.append(man_one)

                    if man_one.in_boat:
                        Boat.count_in_boat -= 1
                        while man_one in Boat.test:
                            Boat.test.remove(man_one)

                    if Boat.count_in_boat < 2:
                        man_one.go_to_boat(boat)

                if event.key == pygame.K_s:

                    if len(Boat.test) < 2 and (man_two.position == boat.position):
                        Boat.test.append(man_two)
                    if man_two.in_boat:
                        Boat.count_in_boat -= 1
                        while man_two in Boat.test:
                            Boat.test.remove(man_two)

                    if Boat.count_in_boat < 2:
                        man_two.go_to_boat(boat)

                if event.key == pygame.K_d:
                    if len(Boat.test) < 2 and (man_three.position == boat.position):
                        Boat.test.append(man_three)
                    if man_three.in_boat:
                        Boat.count_in_boat -= 1
                        while man_three in Boat.test:
                            Boat.test.remove(man_three)

                    if Boat.count_in_boat < 2:
                        man_three.go_to_boat(boat)

                if event.key == pygame.K_f:
                    if len(Boat.test) < 2 and (monster_one.position == boat.position):
                        Boat.test.append(monster_one)
                    if monster_one.in_boat:
                        Boat.count_in_boat -= 1
                        while monster_one in Boat.test:
                            Boat.test.remove(monster_one)

                    if Boat.count_in_boat < 2:
                        monster_one.go_to_boat(boat)

                if event.key == pygame.K_g:
                    if len(Boat.test) < 2 and (monster_two.position == boat.position):
                        Boat.test.append(monster_two)
                    if monster_two.in_boat:
                        Boat.count_in_boat -= 1
                        while monster_two in Boat.test:
                            Boat.test.remove(monster_two)

                    if Boat.count_in_boat < 2:
                        monster_two.go_to_boat(boat)

                if event.key == pygame.K_h:
                    if len(Boat.test) < 2 and (monster_three.position == boat.position):
                        Boat.test.append(monster_three)
                    if monster_three.in_boat:
                        Boat.count_in_boat -= 1
                        while monster_three in Boat.test:
                            Boat.test.remove(monster_three)

                    if Boat.count_in_boat < 2:
                        monster_three.go_to_boat(boat)

                if event.key == pygame.K_SPACE:
                    if len(Boat.test) > 0:
                        boat.row()
                        for data in Boat.test:
                            data.row()

                    if (Boat.right_monster > Boat.right_man) and Boat.right_man > 0:
                        game_lose = True

                    if (Boat.left_monster > Boat.left_man) and Boat.left_man > 0:
                        game_lose = True

                    if Boat.right_monster == 3 and Boat.right_man == 3:
                        game_win = True


if __name__ == '__main__':
    move_left()
