import pygame
import random


def draw(screen, fnt, fnt1, array, arr_color, clr):
    ms_txt = fnt.render("Press m for Merge sort:", 1, (0, 0, 0))
    ms_txt1 = fnt.render("Press b for bubble sort:", 1, (0, 0, 0))
    ms_txt2 = fnt.render("Press s for quick sort:", 1, (0, 0, 0))
    text = fnt1.render("sorting algorithms:--", 1, (0, 0, 0))
    screen.blit(ms_txt, (230, 0))
    screen.blit(ms_txt1, (230, 15))
    screen.blit(ms_txt2, (230, 30))
    screen.blit(text, (0, 0))
    pygame.draw.line(screen, (0, 0, 0), (0, 95), (900, 95), 6)
    for i in range(1,100):
        pygame.draw.line(screen, clr[4], (0, 5.5*i+100), (900, 5.5*i+100), 1)
    for i in range(1,151):
        pygame.draw.line(screen, arr_color[i], (6*i-3, 650), (6*i-3, array[i]*6+100), 5)

def shuffel_arr(array):
    for i in range(151):
        array[i] = random.randrange(1, 90)


def refill(screen, fnt, fnt1, array, arr_color,clr):
    screen.fill(clr[4])
    draw(screen, fnt, fnt1, array, arr_color,clr)
    pygame.display.update()
    pygame.time.delay(20)
