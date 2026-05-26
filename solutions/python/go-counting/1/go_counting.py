BLACK = 'B'
WHITE = 'W'
NONE = ' '
BOUNDARY = 'X'

class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def __init__(self, board):
        self.check_board(board)
        self.height = len(board)
        self.width = len(board[0])
        self.board = self.draw(board)

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        if not 0 <= x < self.width or not 0 <= y < self.height:
            raise ValueError('Invalid coordinate')
        walking_pos = (y + 1, x + 1)
        if self.board[walking_pos[0]][walking_pos[1]] != NONE:
            return NONE, set()
        symbol, positions = self.statistic(walking_pos)
        return symbol, self.modify(positions)

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        result = {BLACK: set(), WHITE: set(), NONE: set()}
        checked = set()
        for row in range(1, self.height + 1):
            for col in range(1, self.width + 1):
                walking_pos = (row, col)
                if self.board[row][col] == NONE and walking_pos not in checked:
                    symbol, positions = self.statistic(walking_pos)
                    result[symbol].update(positions)
                    checked.update(positions)
        for symbol, positions in result.items():
            result[symbol] = self.modify(positions)
        return result

    def check_board(self, board):
        if not board:
            raise ValueError('Empty board!')
        width = len(board[0])
        for row in board:
            if len(row) != width:
                raise ValueError('Invalid board!')
            for char in row:
                if char not in [BLACK, WHITE, NONE]:
                    raise ValueError('Invalid symbol!')

    def draw(self, board):
        board = [[char for char in row] for row in board]
        for i in range(self.height):
            board[i] = [BOUNDARY] + board[i] + [BOUNDARY]
        empty_row = [BOUNDARY] * (self.width + 2)
        return [empty_row] + board + [empty_row]

    def statistic(self, walking_pos):
        checked = set()
        checking = set([walking_pos])
        symbols = set()
        while checking:
            pos = checking.pop()
            for direction in self.DIRECTIONS:
                neighbor = (pos[0] + direction[0], pos[1] + direction[1])
                symbol = self.board[neighbor[0]][neighbor[1]]
                if symbol == NONE:
                    if neighbor not in checked:
                        checking.add(neighbor)
                else:
                    symbols.add(symbol)
            checked.add(pos)
        symbols.discard(BOUNDARY)
        if len(symbols) == 1:
            return symbols.pop(), checked
        return NONE, checked

    def modify(self, positions):
        modified = set()
        for row, col in positions:
            modified.add((col - 1, row - 1))
        return modified

if __name__ == '__main__':
    board = Board([
        "  B  ",
        " B B ",
        "B W B",
        " W W ",
        "  W  ",
    ])
    print(board.territories())
