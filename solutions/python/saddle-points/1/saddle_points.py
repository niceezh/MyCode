import math

def is_matrix(matrix):
    if not isinstance(matrix, list):
        return False
    if not matrix:
        return True
    return all(isinstance(row, list) for row in matrix) and all(isinstance(cell, int) for row in matrix for cell in row) and all(len(row) == len(matrix[0]) for row in matrix)

def pad(matrix):
    row_padded = [[0] + row + [0] for row in matrix]
    pad_row = [math.inf] * len(row_padded[0])
    return [pad_row] + row_padded + [pad_row]

def saddle_points(matrix):
    if not is_matrix(matrix):
        raise ValueError("irregular matrix")
    if not matrix:
        return []
    result = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == max(matrix[row]) and matrix[row][col] == min(matrix[tmp_row][col] for tmp_row in range(len(matrix))):
                result.append({"row": row+1, "column": col+1})
    return result
