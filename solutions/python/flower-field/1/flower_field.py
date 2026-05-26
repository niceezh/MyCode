def annotate(garden: list):
    if not garden:
        return []
    width = len(garden[0])
    for flowers in garden:
        if len(flowers) != width:
            raise ValueError('The board is invalid with current input.')
        for flower in flowers:
            if flower not in [' ', '*']:
                raise ValueError('The board is invalid with current input.')
    height = len(garden)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    result = []
    for row in range(height):
        current = []
        for col in range(width):
            if garden[row][col] == '*':
                current.append('*')
                continue
            count = 0
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < height and 0 <= nc < width and garden[nr][nc] == '*':
                    count += 1
            current.append(str(count) if count else ' ')
        result.append(''.join(current))
    return result

if __name__ == '__main__':
    print(annotate(['     ', '   * ', '     ', '     ', ' *   ']))
