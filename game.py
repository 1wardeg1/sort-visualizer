import time
import pygame
from settings import *
from button import *


class Screen:
    def __init__(self, sc, arr):
        self.sc = sc
        self.arr = arr
        self.step = W / len(arr)
        self.max = max(arr)
        self.active = False
        self.back_button = Button(10, 10, "BACK", True)
        self.exit = False

    def getY(self, num):
        return H - (H * num / self.max)

    def getX(self, elem):
        return elem * self.step

    def sizeY(self, num):
        return H * num / self.max

    def getTimeSec(self):
        return (time.time_ns() // 10 ** 7) / 100

    def safeSleep(self, time):
        t = self.getTimeSec()
        while self.getTimeSec() - t < time:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = 1
                    return
            pygame.display.flip()
            pygame.display.update()

    def draw(self, arr):
        self.sc.fill(scColor)
        cnt = 0
        for num, elem in enumerate(self.arr):
            pygame.draw.rect(self.sc, exchColor if arr[num] != self.arr[num] and cnt <= 4 else arrColor,
                             [self.getX(num),
                              self.getY(elem),
                              self.step,
                              self.sizeY(elem)])
        pygame.display.update()
        self.safeSleep(sleep_time)

    def swap(self, ind1, ind2):
        self.arr[ind1], self.arr[ind2] = self.arr[ind2], self.arr[ind1]

    def start(self, movesF):
        moves, oper = movesF(self.arr)
        print("Operations:", oper)

        self.draw(self.arr)
        for arr in moves:
            if self.exit:
                return
            self.draw(arr)
            self.arr = arr

        self.draw(self.arr)

        while not self.exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                self.active = self.back_button.collide(*pygame.mouse.get_pos())
                if pygame.mouse.get_pressed()[0] and self.active:
                    return

            self.back_button.draw(self.sc, self.active)
            pygame.display.update()
