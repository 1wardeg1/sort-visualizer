from random import randint
from game import *
from sortAlg import *
from settings import *
import pygame
import time
from button import *
from slider import Slider
from checkerbox import CheckerBox


def generateArr(n):
    arr = [0] * n
    for i in range(n):
        arr[i] = randint(1, 100)
    return arr


class Main:
    def __init__(self):
        self.sc = pygame.display.set_mode(res)
        self.slider = Slider(W // 2, H // 3, 10, 40, W // 2, 30, 30, 1, 50)
        self.status = conditions["menu"]
        self.start_button = Button(W // 2, H // 2, "START")
        self.start_button_active = False
        self.choose_back_button = Button(10, 10, "BACK", 1)
        self.exit_button_active = False
        self.exit_button = Button(W // 2,
                                  H // 2 + 2 * delta[1] + self.start_button.h, "EXIT",
                                  rect=[
                                      self.start_button.best_rect[0],
                                      self.start_button.best_rect[1] + 2 * delta[1] + self.start_button.h,
                                      self.start_button.best_rect[2],
                                      self.start_button.best_rect[3]
                                  ])
        self.checkbox_text_and_pos = self.getTextBlit(10, H - 10, "FULL SCREEN:", menu_font, menu_text_color)
        self.checkbox = CheckerBox(self.checkbox_text_and_pos[1] + self.checkbox_text_and_pos[0].get_width() + delta[0],
                                   self.checkbox_text_and_pos[2], self.checkbox_text_and_pos[0].get_height(),
                                   self.checkbox_text_and_pos[0].get_height(), 5)
        pygame.display.set_caption('SORT VISUALIZER')

        self.choose_buttons = self.fillChooseButtons()
        self.active_buttons = [0] * len(self.choose_buttons)

        self.back_active = False

    def getTextBlit(self, x, y, text, font, clr):
        text_sc = font.render(text, True, clr)
        posx = x
        posy = y - text_sc.get_height()
        return [text_sc, posx, posy]

    def fillChooseButtons(self):
        ans = []
        startPos = [W // 7, H // 7]

        wasX = wasY = 0

        for num, alg in enumerate(sortAlgs):
            if num % 1 == 0 and num > 0:
                wasX = 0
                wasY += ans[-1].h + delta[1]
            ans.append(Button(
                startPos[0] + wasX,
                startPos[1] + wasY,
                alg,
                True
            ))

            wasX += ans[-1].w + delta[0]

        return ans

    def draw_text(self, x, y, text, font, clr):
        text_sc = font.render(text, True, clr)
        w, h = text_sc.get_width(), text_sc.get_height()
        posx = x - w // 2
        posy = y - h // 2
        self.sc.blit(text_sc, (posx, posy))

    def draw_menu(self):
        global res, W, H
        self.sc.fill(screenColor)

        self.draw_text(W // 2, H // 10, name, menuFont, menuColor)
        self.start_button.draw(self.sc, self.start_button_active)
        self.exit_button.draw(self.sc, self.exit_button_active)
        self.slider.draw(self.sc)
        self.slider.update()
        self.draw_text(W // 2, H // 3 - 80, f"ARRAY SIZE: {self.slider.get()}", menu_font, menu_text_color)

        pygame.display.update()

    def draw_options(self):
        self.sc.fill(screenColor)

        pygame.display.update()

    def draw_choose(self):
        self.sc.fill(screenColor)
        self.choose_back_button.draw(self.sc, self.back_active)

        for num, button in enumerate(self.choose_buttons):
            button.draw(self.sc, self.active_buttons[num])

        pygame.display.update()

    def start_choose(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                self.back_active = self.choose_back_button.collide(*pygame.mouse.get_pos())
                for num, button in enumerate(self.choose_buttons):
                    self.active_buttons[num] = button.collide(*pygame.mouse.get_pos())
                    if pygame.mouse.get_pressed()[0] and self.active_buttons[num]:
                        self.game = Screen(self.sc, generateArr(self.slider.get()))
                        self.game.start(sortAlgs[button.text])
                        self.game.arr = generateArr(self.slider.get())
                        self.game.exit = False
                        return
                if pygame.mouse.get_pressed()[0] and self.back_active:
                    self.back_active = False
                    return
            self.draw_choose()

    def getTimeSec(self):
        return (time.time_ns() // 10 ** 7) / 100

    def safeSleep(self, time):
        t = self.getTimeSec()
        while self.getTimeSec() - t < time:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
            pygame.display.flip()
            pygame.display.update()

    def start(self):
        flag = True

        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
                self.start_button_active = self.start_button.collide(*pygame.mouse.get_pos())
                self.exit_button_active = self.exit_button.collide(*pygame.mouse.get_pos())
                if pygame.mouse.get_pressed()[0] and self.exit_button_active:
                    print("Bye")
                    exit(0)
                if pygame.mouse.get_pressed()[0] and self.start_button_active:
                    self.status = conditions["game"]

            if self.status == conditions["menu"]:
                self.draw_menu()
            elif self.status == conditions["game"]:
                self.start_button_active = False
                self.safeSleep(0.2)
                self.start_choose()
                self.status = conditions["menu"]


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()

    Main().start()
