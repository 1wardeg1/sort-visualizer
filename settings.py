from sortAlg import *
import pygame
from win32api import GetSystemMetrics

width, height = GetSystemMetrics(0), GetSystemMetrics(1)

pygame.font.init()

name = 'SORT VISUALIZER'

sortAlgs = {"MERGE SORT": mergeSort,
            "BUBBLE SORT": bubbleSort,
            "SELECTION SORT": selectionSort,
            "INSERTION SORT": insertionSort,
            "QUICK SORT": quickSort,
            "HEAP SORT": heapSort,
            "SHELL SORT": shellSort}

slideColor = '#D5CDCD'
buttonSlideColor = '#F4F3F0'
borderSlideColor = '#000000'
checkerColor = '#000000'
checkerActiveColor = '#0AC226'
checkerDeActiveColor = '#F1EEEE'

menu_font = pygame.font.SysFont('comicsans', 32)
menu_text_color = '#1d1d20'
menu_button_color = '#92a292'
menu_color_button_border = '#000000'
active_menu_button_color = '#499e49'

res = W, H = [600, 600]
old_res = res

delta = [20, 20]
arraySize = 80

arrColor = '#b8b8b8'
scColor = '#161616'
exchColor = '#De2727'
screenColor = '#Bbb4a7'
menuColor = (194,83,10)
menuFont = pygame.font.SysFont('comicsans', 40)


sleep_time = 0.01

conditions = {"menu": 0, "game": 1}
