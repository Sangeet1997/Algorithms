

def prime(n):
    '''
    time complexity: O(n log log n)
    space complexity: O(n)
    '''
    
    arr = [True] * (n + 1)
    arr[0] = arr[1] = False
    for i in range (2, int(n**0.5) + 1):
        if arr[i]:
            for j in range(i*i, n + 1, i):
                arr[j] = False
    
    print()
    for i in range(2, n + 1):
        if arr[i]:
            print(i, end = ", ")

prime(100)
