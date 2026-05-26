CODE2NUMBER = {
    "     |  |   ": "1",
    " _  _||_    ": "2",
    " _  _| _|   ": "3",
    "   |_|  |   ": "4",
    " _ |_  _|   ": "5",
    " _ |_ |_|   ": "6",
    " _   |  |   ": "7",
    " _ |_||_|   ": "8",
    " _ |_| _|   ": "9",
    " _ | ||_|   ": "0",
}

def convert(input_grid):
    if len(input_grid) % 4:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(len(line) % 3 for line in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")
    result = []
    for i in range(0, len(input_grid), 4):
        line = []
        for j in range(0, len(input_grid[0]), 3):
            code = "".join(input_grid[i + k][j : j + 3] for k in range(4))
            line.append(CODE2NUMBER[code] if code in CODE2NUMBER else "?")
        result.append("".join(line))
    return ",".join(result)

if __name__ == "__main__":
    print(convert([
        "    _  _     _  _  _  _  _  _ ",
        "  | _| _||_||_ |_   ||_||_|| |",
        "  ||_  _|  | _||_|  ||_| _||_|",
        "                              ",
    ]))
