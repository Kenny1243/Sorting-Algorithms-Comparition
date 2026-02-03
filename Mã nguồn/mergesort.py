import time
import numpy as np

def merge(arr, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid

    A = []
    B = []
    for i in range(0, n1, 1):
        A.append(arr[low + i])
    for j in range(0, n2, 1):
        B.append(arr[mid+1+j])

    i = 0
    j = 0
    k = low 

    while i<n1 and j<n2:
        if A[i]<B[j]:
            arr[k] = A[i]
            i += 1
        else:
            arr[k] = B[j]
            j += 1
        k += 1
    
    while i<n1:
        arr[k] = A[i]
        i += 1
        k += 1
    
    while j<n2:
        arr[k] = B[j]
        j += 1
        k += 1

def mergesort(arr, low, high):
    if low >= high:
        return

    mid = low + (high - low) // 2

    mergesort(arr, low, mid)
    mergesort(arr, mid+1, high)
    merge(arr, low, mid, high)

fi = open('data10.txt')
arr = list(map(float,fi.read().split()))

start = time.perf_counter()
mergesort(arr, 0, len(arr)-1)
end = time.perf_counter()

print(f"{(end - start) * 1000 :.0f}")