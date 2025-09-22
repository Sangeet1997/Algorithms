# trick for inplace rotation:
# 1. transpose
# 2. reverse rows
def rotate(matrix):
    '''
    time complexity : O(n)
    space complexity : O(1)
    '''
    r = len(matrix)
    c = len(matrix[0])

    # transpose
    for i in range(r):
        for j in range(i+1,c):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse rows
    for i in range(r):
        for j in range(0,c//2):
            matrix[i][j], matrix[i][c-j-1] = matrix[i][c-j-1], matrix[i][j]







# Example 1: 3x3 matrix
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Original 3x3 matrix:")
for row in matrix1:
    print(row)
rotate(matrix1)
print("After 90° clockwise rotation:")
for row in matrix1:
    print(row)

# Example 2: 4x4 matrix
matrix2 = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
]
print("\nOriginal 4x4 matrix:")
for row in matrix2:
    print(row)
rotate(matrix2)
print("After 90° clockwise rotation:")
for row in matrix2:
    print(row)

# Example 3: 2x2 matrix
matrix3 = [
    [1, 2],
    [3, 4]
]
print("\nOriginal 2x2 matrix:")
for row in matrix3:
    print(row)
rotate(matrix3)
print("After 90° clockwise rotation:")
for row in matrix3:
    print(row)

# Example 4: Matrix with letters
matrix4 = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I']
]
print("\nOriginal matrix with letters:")
for row in matrix4:
    print(row)
rotate(matrix4)
print("After 90° clockwise rotation:")
for row in matrix4:
    print(row)

