class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        height, width = len(puzzle), len(puzzle[0])
        self.puzzle = []
        for row in puzzle:
            chars = [char for char in row]
            self.puzzle.append(chars)
        for i in range(height):
            self.puzzle[i] = ['*'] + self.puzzle[i] + ['*']
        empty_line = ['*'] * (width + 2)
        self.puzzle = [empty_line] + self.puzzle + [empty_line]

    def search(self, word):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for row in range(1, len(self.puzzle) - 1):
            for col in range(1, len(self.puzzle[row]) - 1):
                if self.puzzle[row][col] == word[0]:
                    start_point = Point(col, row)
                    for direction in directions:
                        end_point = start_point
                        find = True
                        for i in range(1, len(word)):
                            end_point = Point(end_point.x + direction[0], end_point.y + direction[1])
                            if self.puzzle[end_point.y][end_point.x] != word[i]:
                                find = False
                                break
                        if find:
                            start_point = Point(start_point.x - 1, start_point.y - 1)
                            end_point = Point(end_point.x - 1, end_point.y - 1)
                            return (start_point, end_point)


if __name__ == '__main__':
    puzzle = WordSearch(
        [
            "jefblpepre",
            "camdcimgtc",
            "oivokprjsm",
            "pbwasqroua",
            "rixilelhrs",
            "wolcqlirpc",
            "screeaumgr",
            "alxhpburyi",
            "jalaycalmp",
            "clojurermt",
        ])
    result = puzzle.search('clojure')
    if result:
        print(result[0].x, result[0].y, result[1].x, result[1].y)
