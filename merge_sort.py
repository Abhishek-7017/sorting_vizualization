import pygame
import program_functions as pf


def mergesort(array, l, r, arr_clr, clr, screen, fnt, fnt1):
    mid = (l + r) // 2
    if l < r:
        mergesort(array, l, mid, arr_clr, clr, screen, fnt, fnt1)
        mergesort(array, mid + 1, r, arr_clr, clr, screen, fnt, fnt1)
        merge(array, l, mid, mid + 1, r, arr_clr, clr, screen, fnt, fnt1)


def merge(array, x1, y1, x2, y2, arr_clr, clr, screen, fnt, fnt1):
    i = x1
    j = x2
    temp = []
    pygame.event.pump()
    while i <= y1 and j <= y2:
        arr_clr[i] = clr[1]
        arr_clr[j] = clr[1]
        pf.refill(screen, fnt, fnt1, array, arr_clr, clr)
        arr_clr[i] = clr[0]
        arr_clr[j] = clr[0]
        if array[i] < array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
    while i <= y1:
        arr_clr[i] = clr[1]
        pf.refill(screen, fnt, fnt1, array, arr_clr,clr)
        arr_clr[i] = clr[0]
        temp.append(array[i])
        i += 1
    while j <= y2:
        arr_clr[j] = clr[1]
        pf.refill(screen, fnt, fnt1, array, arr_clr,clr)
        arr_clr[j] = clr[0]
        temp.append(array[j])
        j += 1
    j = 0
    for i in range(x1, y2 + 1):
        pygame.event.pump()
        array[i] = temp[j]
        j += 1
        arr_clr[i] = clr[2]
        pf.refill(screen, fnt, fnt1, array, arr_clr, clr)
        if y2 - x1 == len(array) - 2:
            arr_clr[i] = clr[3]
        else:
            arr_clr[i] = clr[0]