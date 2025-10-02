class Disjoint_set:
    def __init__(self):
        self.p = {}
        self.rank = {}

    def find(self, x):

        if x not in self.p:
            return -1
        
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        
        return self.p[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == -1 and parent_y == -1:
            self.p[x] = x
            self.p[y] = x
            self.rank[x] = 1
            self.rank[y] = 0
            return
        
        if parent_x == -1:
            self.p[x] = parent_y
            self.rank[x] = 0
            return

        if parent_y == -1:
            self.p[y] = parent_x
            self.rank[y] = 0
            return
        
        if parent_x != parent_y:
            if self.rank[parent_x] > self.rank[parent_y]:
                self.p[parent_y] = parent_x
                self.p[y] = parent_x

            elif self.rank[parent_y] > self.rank[parent_x]:
                self.p[parent_x] = parent_y
                self.p[x] = parent_y
            
            else:
                self.p[parent_y] = parent_x
                self.p[y] = parent_x
                self.rank[parent_x] += 1
            
                


            


def mst(arr):
    """
    Find Minimum Spanning Tree using Kruskal's algorithm.
    
    Args:
        arr: List of edges [weight, vertex1, vertex2]
    
    Returns:
        List of edges in the MST
    """

    dj_set = Disjoint_set()
    arr.sort()
    res = []
    
    for dist, x, y in arr:
        parent_x = dj_set.find(x)
        parent_y = dj_set.find(y)

        if parent_x == -1 or parent_y == -1 or parent_x != parent_y:
            res.append([dist, x, y])
            dj_set.union(x,y)
        
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
