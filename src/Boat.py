import pygame

boat_jpg = pygame.image.load('images\\boat.png')


class Boat(object):
    count_in_boat = 0

    first = None
    second = None

    position = 'left'

    left_man = 3
    left_monster = 3

    right_man = 0
    right_monster = 0

    test = list()

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw_boat(self, win):
        win.blit(boat_jpg, (self.x, self.y))

    def row(self):
        if self.x == 330:
            self.x += 200
            self.position = 'right'
        elif self.x == 530:
            self.x -= 200
            self.position = 'left'

    def boat_right(self):
        self.x -= 200
