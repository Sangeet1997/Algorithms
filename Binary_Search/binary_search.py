

def binary_search(arr, ele):
    """
    time: O(log n)
    space: O(1)
    """

    l = 0
    r = len(arr) - 1

    while l < r:
        # check mid
        m = (l + r)//2

        # if mid == ele return index
        if ele == arr[m]:
            return m

        # if ele is smaller, ele on left side
        elif ele < arr[m]:
            r = m - 1

        # if ele is larger, ele on right side
        else:
            l = m + 1
    
    return -1
    