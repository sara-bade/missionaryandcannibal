import pygame

from src import Boat

pygame.init()

stop = 0
left = 1
right = 2


# noinspection PyChainedComparisons
class Man(object):
    man_jpg = pygame.image.load('images\\standing.png')
    in_boat = False
    type = 'Man'

    position = 'left'

    def __init__(self, x, y, width, height, name):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win):
        win.blit(self.man_jpg, (self.x, self.y))

    def go_to_boat(self, boat):

        if (self.x >= 380 and self.x <= 420) and boat.position == 'left':
            self.x -= 200
            self.in_boat = False

        elif (self.x >= 780 and self.x <= 820) and boat.position == 'right':
            self.x -= 200
            self.in_boat = True
            Boat.count_in_boat += 1

        elif (self.x >= 180 and self.x <= 220) and boat.position == 'left':
            self.x += 200
            Boat.count_in_boat += 1
            self.in_boat = True

        elif (self.x >= 580 and self.x <= 620) and boat.position == 'right':
            self.x += 200
            self.in_boat = False

    def row(self):
        if self.x >= 380 and self.x <= 420:
            self.x += 200
            self.position = 'right'
            Boat.left_man -= 1
            Boat.right_man += 1

        elif self.x >= 580 and self.x <= 620:
            self.x -= 200
            self.position = 'left'

            Boat.left_man += 1
            Boat.right_man -= 1

    def get_type(self):
        return self.name
