from settings import *
import pygame


class Button:
    def __init__(self, x, y, text, f=False, rect=[-1, -1]):
        if f:
            self.delta = 0
            self.text = text
            self.x, self.y, self.w, self.h, self.txt = *self.rect, self.txt = self.get(x, y, text, f)
            self.best_rect = self.rect
        else:
            self.x, self.y, self.w, self.h, self.txt = *self.rect, self.txt = self.get(x, y, text)
            self.text = text
            self.delta = 20
            self.best_rect = [self.x - self.delta, self.y - self.delta,
                              self.w + self.delta, self.h + self.delta]
            if rect[0] != -1:
                self.best_rect = rect

    def get(self, x, y, text, f=False):
        text_sc = menu_font.render(text, True, menu_text_color)
        w, h = text_sc.get_width(), text_sc.get_height()
        if f:
            return [x, y, w, h, text_sc]
        posx = x - w // 2
        posy = y - h // 2
        return [posx, posy, w, h, text_sc]

    def draw(self, sc: pygame.Surface, active):
        pygame.draw.rect(sc, active_menu_button_color if active else menu_button_color,
                         self.best_rect)
        pygame.draw.rect(sc, menu_color_button_border,
                         self.best_rect, 2)
        sc.blit(self.txt, (self.x - self.delta // 2, self.y - self.delta // 2))

    def collide(self, x, y):
        x -= self.best_rect[0]
        y -= self.best_rect[1]
        return 0 <= x <= self.best_rect[2] and 0 <= y <= self.best_rect[3]
