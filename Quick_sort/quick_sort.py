

def quick_sort(arr,i,j):
    """
    take last element as pivot
    all smaller elements to the left
    all larger element to the right
    """
    if i >= j:
        return
    left = []
    right = []
    pivot = arr[j]

    for ele in arr[i:j]:
        if ele <= pivot:
            left.append(ele)
        else:
            right.append(ele)

    kl = 0
    km = 0
    kr = 0
    for k in range(i,j+1):
        if kl < len(left):
            arr[k] = left[kl]
            kl += 1
        elif km == 0:
            arr[k] = pivot
            km = 1
        else:
            arr[k] = right[kr]
            kr += 1

    quick_sort(arr, i, len(left)+i - 1) # left part
    quick_sort(arr, len(left)+i+1, j) # right part

    pass

import random

arr = []

for i in range(10):
    arr.append(random.randint(0, 9))
print(arr)

quick_sort(arr, 0, len(arr)-1)
print(arr)