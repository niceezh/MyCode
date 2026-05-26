def is_matrix(matrix):
    if not isinstance(matrix, list):
        return False
    if not matrix:
        return True
    return all(isinstance(row, list) for row in matrix) and all(isinstance(cell, int) for row in matrix for cell in row) and all(len(row) == len(matrix[0]) for row in matrix)

def pad(matrix):
    row_padded = [[0] + row + [0] for row in matrix]
    pad_row = [0] * len(row_padded[0])
    return [pad_row] + row_padded + [pad_row]

def tick(matrix):
    if not is_matrix(matrix):
        raise ValueError("Invalid matrix")
    if not matrix:
        return []
    row_size = len(matrix)
    col_size = len(matrix[0])
    padded_matrix = pad(matrix)
    for row in range(1, row_size+1):
        for col in range(1, col_size+1):
            live_neighbors = padded_matrix[row-1][col-1] + padded_matrix[row-1][col] + padded_matrix[row-1][col+1] + padded_matrix[row][col-1] + padded_matrix[row][col+1] + padded_matrix[row+1][col-1] + padded_matrix[row+1][col] + padded_matrix[row+1][col+1]
            if live_neighbors == 2:
                continue
            if live_neighbors == 3:
                matrix[row-1][col-1] = 1
                continue
            matrix[row-1][col-1] = 0
    return matrix

if __name__ == "__main__":
    print(tick([[1, 0, 1], [1, 0, 1], [1, 0, 1]]))
