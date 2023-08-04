from settings import *
import pygame


class CheckerBox:
    def __init__(self, x, y, w, h, delta):
        self.rect = [x, y, w, h]
        self.delta = delta
        self.activated = False

    def draw(self, sc: pygame.Surface):
        pygame.draw.rect(sc, checkerColor, self.rect)
        pygame.draw.rect(sc, checkerActiveColor if self.activated else checkerDeActiveColor, [
            self.rect[0] + self.delta,
            self.rect[1] + self.delta,
            self.rect[2] - 2 * self.delta,
            self.rect[3] - 2 * self.delta
        ])

    def collide(self, x, y):
        x -= self.rect[0]
        y -= self.rect[1]
        return 0 <= x <= self.rect[2] and 0 <= y <= self.rect[3]

    def check(self):
        pos = pygame.mouse.get_pos()
        if self.collide(*pos) and pygame.mouse.get_pressed()[0]:
            return True
        return False
