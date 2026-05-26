class ConnectGame:
    def __init__(self, board):
        if not board.strip():
            raise ValueError("Empty board!")
        rows = board.split("\n")
        self.height = len(rows)
        self.width = len(rows[0].split())
        self.board = []
        for row in rows:
            chars = row.split()
            if len(chars) != self.width:
                raise ValueError("Invalid board!")
            self.board.append(chars)
        self.pad()

    def get_winner(self):
        directions = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)]
        checked_X = set()
        checking_X = set((i, 1) for i in range(1, self.height + 1) if self.board[i][1] == 'X')
        while checking_X:
            pos = checking_X.pop()
            if pos[1] == self.width:
                return 'X'
            for direction in directions:
                neighbor = (pos[0] + direction[0], pos[1] + direction[1])
                if self.board[neighbor[0]][neighbor[1]] == 'X':
                    if neighbor[1] == self.width:
                        return 'X'
                    if neighbor not in checked_X:
                        checking_X.add(neighbor)
            checked_X.add(pos)
        checked_O = set()
        checking_O = set((1, j) for j in range(1, self.width + 1) if self.board[1][j] == 'O')
        while checking_O:
            pos = checking_O.pop()
            if pos[0] == self.height:
                return 'O'
            for direction in directions:
                neighbor = (pos[0] + direction[0], pos[1] + direction[1])
                if self.board[neighbor[0]][neighbor[1]] == 'O':
                    if neighbor[0] == self.height:
                        return 'O'
                    if neighbor not in checked_O:
                        checking_O.add(neighbor)
            checked_O.add(pos)
        return ''

    def pad(self):
        for i in range(self.height):
            self.board[i] = [' '] + self.board[i] + [' ']
        empty_row = [' '] * (self.width + 2)
        self.board = [empty_row] + self.board + [empty_row]

if __name__ == "__main__":
    game = ConnectGame(
        """O X X X X X X X X
            O X O O O O O O O
             O X O X X X X X O
              O X O X O O O X O
               O X O X X X O X O
                O X O O O X O X O
                 O X X X X X O X O
                  O O O O O O O X O
                   X X X X X X X X O"""
    )
    print(game.get_winner())
