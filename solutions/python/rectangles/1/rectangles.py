def rectangles(strings):
    graph = []
    for string in strings:
        graph.append([char for char in string])
    if len(graph) < 2 or len(graph[0]) < 2:
        return 0
    count = 0
    row, col = len(graph), len(graph[0])
    for i in range(row-1):
        for j in range(col-1):
            if graph[i][j] == '+':
                for p in range(i+1, row):
                    if graph[p][j] == '+' and is_line(graph, i, j, p, j):
                        for q in range(j+1, col):
                            if graph[i][q] == '+' and is_line(graph, i, j, i, q):
                                if graph[p][q] == '+' and is_line(graph, p, j, p, q) and is_line(graph, i, q, p, q):
                                    count += 1
    return count

def is_line(graph, a1, b1, a2, b2):
    if a1 != a2 and b1 != b2:
        return False
    if a1 == a2:
        for b in range(b1+1, b2):
            if graph[a1][b] not in ['+', '-']:
                return False
        return True
    if b1 == b2:
        for a in range(a1+1, a2):
            if graph[a][b1] not in ['+', '|']:
                return False
        return True
    return False

if __name__ == '__main__':
    print(rectangles(
        [
            "  +-+",
            "    |",
            "+-+-+",
            "| | -",
            "+-+-+",
        ]
    ))
