combo = []
combo = [[1, 0], [0, 1], [2, 0], [0, 2], [1, 1]]
live_state = []
dead_state = []
import pygame, sys
from pygame.locals import *
import os

pygame.init()
height = 700
weidth = 1200
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
fps = 60
screen = pygame.display.set_mode((weidth, height))
screen.fill(white)
pygame.display.set_caption('Game Tree')
done = False
clock = pygame.time.Clock()
stx = 400
sty = 60
rx = 25
ry = 12
tree = []
font = pygame.font.SysFont("dejavusans", 9)

rec1 = pygame.image.load('images\\rect1.png')
rec2 = pygame.image.load('images\\rect2.png')
rec3 = pygame.image.load('images\\rect3.png')
rec4 = pygame.image.load('images\\rect4.png')

while not done:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    class state:
        def __init__(self, c, m, pos):
            self.c = c
            self.m = m
            self.pos = pos
            self.is_dead = False
            self.parent = None
            self.is_finished = False
            self.x = stx
            self.y = sty


    def search_state(c, m, pos, tree):
        n = len(tree)
        check = False
        for i in range(n):
            if c == tree[i][0] and m == tree[i][1] and pos == tree[i][2]:
                check = True
                x = tree[i][3]
                y = tree[i][4]
                break
        if check == True:
            return (True, x, y)
        else:
            return (False, 0, 0)


    def state_tree(space, xpass, ypass):

        xs = space.x + (rx // 2)
        ys = space.y + ry
        ye = ys + 55
        ad = 60
        check = False
        if ye > ypass:
            xe = 190
        else:
            xe = xpass + ad

        for i in range(5):
            space1 = state(space.c, space.m, space.pos)

            c1 = combo[i][0]
            m1 = combo[i][1]
            space1.pos = (space.pos + 1) % 2
            '''if space.pos==0 and (i==0 or i==1):
            	continue
            if space.combo_used==combo[i]:
            	continue'''
            if space.pos == 0:

                space1.c = space.c - c1

                space1.m = space.m - m1
            else:
                space1.c = space.c + c1
                space1.m = space.m + m1
            space1.parent = space
            data = "[" + str(space1.c) + "," + str(space1.m) + "," + str(space1.pos) + "] (" + str(c1) + "," + str(
                m1) + ")"
            text = font.render(data, True, black)
            if space1.pos == 0:
                if space1.c < c1 or space1.m < m1:
                    space1.is_dead = True
            elif space1.pos == 1:
                if (3 - space1.c) < c1 or (3 - space1.m) < m1:
                    space1.is_dead = True
            check, x, y = search_state(space1.c, space1.m, space1.pos, tree)
            print(check)
            if space1.c == 0 and space1.m == 0 and space1.pos == 1:
                space1.is_finished = True
                pygame.draw.line(screen, black, [xs, ys], [xe, ye], 1)
                screen.blit(rec3, (xe, ye))
                screen.blit(text, (xe, ye))
                xe = xe + ad
            elif (space1.is_dead == True):
                pygame.draw.line(screen, black, [xs, ys], [xe, ye], 1)
                screen.blit(rec2, (xe, ye))
                screen.blit(text, (xe, ye))
                xe = xe + ad
            elif space1.c > space1.m or space1.c < 0 or space1.m < 0 or space1.c > 3 or space1.m > 3:
                space1.is_dead = True
                pygame.draw.line(screen, black, [xs, ys], [xe, ye], 1)
                screen.blit(rec2, (xe, ye))
                screen.blit(text, (xe, ye))
                xe = xe + ad
            elif check == True:
                space1.is_dead = True
                pygame.draw.line(screen, black, [xs, ys], [xe, ye], 1)
                pygame.draw.line(screen, blue, [xe, ye], [x, y], 1)
                screen.blit(rec4, (xe, ye))
                screen.blit(text, (xe, ye))
                xe = xe + ad
            else:
                space1.x = xe
                space1.y = ye
                pygame.draw.line(screen, black, [xs, ys], [xe, ye], 1)
                screen.blit(rec1, (xe, ye))
                screen.blit(text, (xe, ye))
                xe = xe + ad

                b = []
                b.append(space1.c)
                b.append(space1.m)
                b.append(space1.pos)
                b.append(space1.x)
                b.append(space1.y)
                tree.append(b)
                live_state.append(space1)
        if (len(live_state) == 0):
            print("-----------Game Finished--------------")

        else:
            space = live_state.pop(0)
            state_tree(space, xe, ye)
        pygame.display.flip()


    st = state(3, 3, 0)
    screen.blit(rec1, (stx, sty))
    text = font.render("[3,3,0]", True, black)
    screen.blit(text, (stx, sty))
    state_tree(st, stx, sty)
    txt = font.render("Live State", True, black)
    screen.blit(rec1, (1000, 5))
    screen.blit(txt, (1030, 5))
    txt = font.render("Dead State", True, black)
    screen.blit(rec2, (1000, 20))
    screen.blit(txt, (1030, 20))
    txt = font.render("Goal State", True, black)
    screen.blit(rec3, (1000, 35))
    screen.blit(txt, (1030, 35))
    txt = font.render("Visited State", True, black)
    screen.blit(rec4, (1000, 50))
    screen.blit(txt, (1030, 50))
    font1 = pygame.font.SysFont("dejavusans", 30)
    txt = font1.render("State Space Of Cannibal And Missionary Game", True, black)
    screen.blit(txt, (250, 5))
pygame.quit()
