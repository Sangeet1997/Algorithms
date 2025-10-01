def mst(arr): # array with each elements as [distance, x , y]

    visited = set()
    arr.sort()
    res = []
    
    for dist, x, y in arr:
        if x in visited and y in visited:
            continue
        res.append([dist,x,y])
        visited.add(x)
        visited.add(y)

    return res

if __name__ == "__main__":
    # Test case 1: Simple triangle graph
    # Vertices: 0, 1, 2
    # Edges: (0,1)=1, (1,2)=2, (0,2)=3
    edges1 = [
        [1, 0, 1],
        [2, 1, 2],
        [3, 0, 2]
    ]
    print("Test 1 - Triangle graph:")
    print("Input:", edges1)
    print("MST:", mst(edges1))
    print("Expected: [[1, 0, 1], [2, 1, 2]]")
    print()
    
    # Test case 2: Square graph with diagonal
    # Vertices: 0, 1, 2, 3
    edges2 = [
        [4, 0, 1],
        [8, 0, 2],
        [11, 1, 2],
        [8, 1, 3],
        [2, 2, 3],
        [7, 0, 3]
    ]
    print("Test 2 - Square with diagonal:")
    print("Input:", edges2)
    print("MST:", mst(edges2))
    print("Expected: [[2, 2, 3], [4, 0, 1], [7, 0, 3]]")
    print()
    
    # Test case 3: Linear graph
    # Vertices: A, B, C, D (represented as strings)
    edges3 = [
        [1, 'A', 'B'],
        [3, 'B', 'C'],
        [2, 'C', 'D'],
        [5, 'A', 'C'],
        [4, 'B', 'D']
    ]
    print("Test 3 - Linear graph:")
    print("Input:", edges3)
    print("MST:", mst(edges3))
    print("Expected: [[1, 'A', 'B'], [2, 'C', 'D'], [3, 'B', 'C']]")
    print()
    
    # Test case 4: Disconnected graph (should connect all possible)
    edges4 = [
        [1, 0, 1],
        [2, 2, 3],
        [10, 0, 2]  # This connects the two components
    ]
    print("Test 4 - Initially disconnected:")
    print("Input:", edges4)
    print("MST:", mst(edges4))
    print()
