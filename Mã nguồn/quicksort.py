import numpy as np
import time
import sys
sys.setrecursionlimit(1_500_000)

def partition(arr, low, high):
    #pivot choosing
    rand = np.random.randint(low, high)
    arr[rand], arr[high] = arr[high],arr[rand]
    pivot = arr[high]

    i = low - 1
    for j in range(low, high, 1):
        if arr[j]<pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quicksort(arr, low, high):
     if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

fi = open('data10.txt')
#s = int(fi.readline())
arr = list(map(float,fi.read().split()))

start_time = time.perf_counter()
quicksort(arr, 0, len(arr) - 1  )
end_time = time.perf_counter()

print (f"{(end_time - start_time)*1000:.0f}")
