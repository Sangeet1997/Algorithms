
def max_sum(arr):
    '''
    time complexity: O(n)
    space complexity: O(1)
    '''
    subarray_sum = 0
    res = -float('inf')

    for ele in arr:
        subarray_sum = max(subarray_sum + ele, ele)
        res = max(res,subarray_sum)
    
    return res

if __name__ == "__main__":
    # Test case 1: Mixed positive and negative numbers
    test1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Array: {test1}")
    print(f"Maximum subarray sum: {max_sum(test1)}")  # Expected: 6 (subarray [4, -1, 2, 1])
    print()
    
    # Test case 2: All negative numbers
    test2 = [-5, -2, -8, -1]
    print(f"Array: {test2}")
    print(f"Maximum subarray sum: {max_sum(test2)}")  # Expected: -1
    print()
    
    # Test case 3: All positive numbers
    test3 = [1, 2, 3, 4, 5]
    print(f"Array: {test3}")
    print(f"Maximum subarray sum: {max_sum(test3)}")  # Expected: 15
    print()
    
    # Test case 4: Single element
    test4 = [42]
    print(f"Array: {test4}")
    print(f"Maximum subarray sum: {max_sum(test4)}")  # Expected: 42
    print()
    
    # Test case 5: Zero included
    test5 = [-1, 0, -2, 3, 0, -1, 2]
    print(f"Array: {test5}")
    print(f"Maximum subarray sum: {max_sum(test5)}")  # Expected: 4