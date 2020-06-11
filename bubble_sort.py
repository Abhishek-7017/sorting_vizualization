import program_functions as pf


def bubblesort(array, arr_clr, clr, screen, fnt, fnt1):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                arr_clr[j] = clr[1]
                arr_clr[j+1] = clr[1]
                pf.refill(screen, fnt, fnt1, array, arr_clr, clr)
                arr_clr[j] = clr[0]
                arr_clr[j+1] = clr[0]
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    for i in range(0, n):
        arr_clr[i] = clr[3]
        pf.refill(screen, fnt, fnt1, array, arr_clr, clr)
