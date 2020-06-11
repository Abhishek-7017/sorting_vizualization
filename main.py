import sys
import pygame
import program_functions as pf
import merge_sort as ms
import bubble_sort as bs
import quicksort as qs
from settings import Setting


def run_program():
    pygame.init()
    screen = pygame.display.set_mode((900, 650))
    sr_setting = Setting()
    pygame.display.set_caption("Sorting alogrithms")
    fnt = pygame.font.SysFont("comicsans", 25)
    fnt1 = pygame.font.SysFont("comicsans", 30)
    array = [0]*151
    arr_color = [sr_setting.Green]*151
    clr = [sr_setting.Green, sr_setting.Red, sr_setting.Dark_blue, sr_setting.Orange, sr_setting.bg_color]
    pf.shuffel_arr(array)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_m:
                    ms.mergesort(array, 1, len(array)-1, arr_color, clr, screen, fnt, fnt1)
                if event.key == pygame.K_b:
                    bs.bubblesort(array, arr_color, clr, screen, fnt, fnt1)
                if event.key == pygame.K_s:
                    qs.quicksort(array, arr_color, clr, screen, fnt, fnt1)
        screen.fill(sr_setting.bg_color)
        pf.draw(screen, fnt, fnt1, array, arr_color, clr)
        pygame.display.flip()


if __name__ == "__main__":
    run_program()
