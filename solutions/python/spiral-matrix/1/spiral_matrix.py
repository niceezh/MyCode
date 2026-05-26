def spiral_matrix(size):
    """
    Generates a spiral matrix of size n x n.
    """
    matrix = [[0] * size for _ in range(size)]
    top, left, bottom, right = 0, 0, size - 1, size - 1
    num = 1
    while num <= size * size:
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1
        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1
        for col in range(right, left - 1, -1):
            matrix[bottom][col] = num
            num += 1
        bottom -= 1
        for row in range(bottom, top - 1, -1):
            matrix[row][left] = num
            num += 1
        left += 1
    return matrix

if __name__ == '__main__':
    print(spiral_matrix(5))
