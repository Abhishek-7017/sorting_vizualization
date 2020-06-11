import program_functions as pf


def partition(arr, low, high, arr_color, clr, screen, fnt, fnt1):
        i = (low-1)
        pivot = arr[high]

        for j in range(low, high):
                arr_color[j] = clr[1]
                arr_color[high] = clr[1]
                pf.refill(screen, fnt, fnt1, arr, arr_color, clr)
                arr_color[j] = clr[0]
                arr_color[high] = clr[0]
                if arr[j] < pivot:
                        i = i+1
                        arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)


def quickSort(arr, low, high, arr_color, clr, screen, fnt, fnt1):
        if low<high:
                pi = partition(arr, low, high, arr_color, clr, screen, fnt, fnt1)
                quickSort(arr, low, pi-1, arr_color, clr, screen, fnt, fnt1)
                quickSort(arr, pi+1, high, arr_color, clr, screen, fnt, fnt1)


def quicksort(array, arr_color, clr, screen, fnt, fnt1):
        low = 0
        high = len(array)-1
        quickSort(array,low,high, arr_color, clr, screen, fnt, fnt1)