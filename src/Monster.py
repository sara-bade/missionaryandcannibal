import pygame

from src import Boat

pygame.init()


# noinspection PyChainedComparisons
class Monster(object):
    monster_jpg = pygame.image.load('images\\reuk.png')
    in_boat = False

    type = 'Monster'

    position = 'left'

    def __init__(self, x, y, width, height, name):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win):
        win.blit(self.monster_jpg, (self.x, self.y))

    def go_to_boat(self, boat):

        if (self.x >= 320 and self.x <= 360) and boat.position == 'left':
            self.x -= 200
            self.in_boat = False

        elif (self.x >= 720 and self.x <= 760) and boat.position == 'right':
            self.x -= 200
            self.in_boat = True
            Boat.count_in_boat += 1

        elif (self.x >= 120 and self.x <= 160) and boat.position == 'left':
            self.x += 200
            Boat.count_in_boat += 1
            self.in_boat = True

        elif (self.x >= 520 and self.x <= 560) and boat.position == 'right':
            self.x += 200
            self.in_boat = False

    def row(self):
        if self.x >= 320 and self.x <= 360:
            self.x += 200
            self.position = 'right'
            Boat.left_monster -= 1
            Boat.right_monster += 1

        elif self.x >= 520 and self.x <= 560:
            self.x -= 200
            self.position = 'left'

            Boat.left_monster += 1
            Boat.right_monster -= 1

    def get_type(self):
        return self.name
