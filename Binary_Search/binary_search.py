def binary_search(arr, ele):
    """
    time: O(log n)
    space: O(1)
    """

    l = 0
    r = len(arr) - 1

    while l <= r:
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



# Test the binary search function
if __name__ == "__main__":
    # Test arrays (must be sorted for binary search)
    test_arrays = [
        [1, 3, 5, 7, 9, 11, 13],
        [2, 4, 6, 8, 10],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [5],
        []
    ]
    
    # Test cases: (array_index, element_to_find, expected_result)
    test_cases = [
        (0, 7, 3),      # Element exists in middle
        (0, 1, 0),      # Element at beginning
        (0, 13, 6),     # Element at end
        (0, 4, -1),     # Element doesn't exist
        (1, 6, 2),      # Element exists
        (1, 1, -1),     # Element doesn't exist
        (2, 5, 4),      # Element in larger array
        (3, 5, 0),      # Single element array - found
        (3, 3, -1),     # Single element array - not found
        (4, 1, -1),     # Empty array
    ]
    
    print("Testing Binary Search Implementation:")
    print("=" * 40)
    
    for i, (arr_idx, element, expected) in enumerate(test_cases):
        arr = test_arrays[arr_idx]
        result = binary_search(arr, element)
        status = "✓" if result == expected else "✗"
        
        print(f"Test {i+1}: {status}")
        print(f"  Array: {arr}")
        print(f"  Searching for: {element}")
        print(f"  Expected: {expected}, Got: {result}")
        print()


