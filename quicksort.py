def quicksort(arr, lo, hi):
    if lo < hi:
        pi = partition(arr, lo, hi)
        quicksort(arr, lo, pi - 1)
        quicksort(arr, pi + 1, hi)

def partition(arr, lo, hi):
    pivot = hi
    i = lo
    for j in range(lo, hi-1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i