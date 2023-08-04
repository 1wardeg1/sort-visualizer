from settings import *
import pygame


def upd(val):
    global arraySize
    arraySize = val


class Slider:
    def __init__(self, x, y, sliderW, sliderH, buttonW, buttonH, value, minValue, maxValue):
        self.rect = [x - buttonW // 2,
                     y - buttonH // 2,
                     buttonW,
                     buttonH]
        self.rng = [minValue, maxValue]
        self.value = value
        self.slider = [sliderW, sliderH]

    def getSliderButtonRect(self):
        return [self.rect[0] + ((self.value - self.rng[0]) / (self.rng[1] - self.rng[0])) * self.rect[2] - self.slider[0] / 2,
                self.rect[1] + self.rect[3] // 2 - self.slider[1] // 2,
                *self.slider]

    def get(self):
        v = int(self.value ** 1.6)
        return v

    def draw(self, sc):
        pygame.draw.rect(sc, slideColor,
                         [
                             self.rect[0] - self.slider[0] // 2,
                             self.rect[1],
                             self.rect[2] + self.slider[0] // 2,
                             self.rect[3]
                         ])
        pygame.draw.rect(sc, buttonSlideColor, self.getSliderButtonRect())
        pygame.draw.rect(sc, borderSlideColor, self.getSliderButtonRect(), 1)

    def collide(self, x, y):
        x -= self.rect[0]
        y -= self.rect[1]
        return 0 <= x <= self.rect[2] and 0 <= y <= self.rect[2]

    def update(self):
        x, y = pygame.mouse.get_pos()
        if self.collide(x, y) and pygame.mouse.get_pressed()[0]:
            self.value = (x - self.rect[0]) / self.rect[2] * (self.rng[1] - self.rng[0]) + self.rng[0]
