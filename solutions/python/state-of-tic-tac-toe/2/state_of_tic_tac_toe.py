"""
Module for checking the game state of a Tic-Tac-Toe board.

This module provides functions to validate the board state, count player moves,
check for winning conditions, and determine if the game is a win, draw, or ongoing.
"""

def is_player_winner(board, player):
    """
    Check if the specified player (X/O) has won the Tic-Tac-Toe game.
    
    A win is defined as:
    - 3 in a row (horizontal)
    - 3 in a column (vertical)
    - 3 in a diagonal (top-left to bottom-right or top-right to bottom-left)
    
    Args:
        board: List of 3 strings (each 3 characters) representing the Tic-Tac-Toe board
        player: String ("X" or "O") representing the player to check
    
    Returns:
        bool: True if the player has won, False otherwise
    """
    if player * 3 in board:
        return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return any(board[0][i] == board[1][i] == board[2][i] == player for i in range(3))

def count_player_moves(board, player):
    """
    Count the number of moves made by the specified player on the board.
    
    Args:
        board: List of 3 strings (each 3 characters) representing the Tic-Tac-Toe board
        player: String ("X" or "O") representing the player to count
    
    Returns:
        int: Total number of the player's marks on the board
    """
    return sum(row.count(player) for row in board)

def gamestate(board):
    """
    Determine the current state of the Tic-Tac-Toe game and validate turn order.
    
    Valid game states:
    - "win": A player has won (game over)
    - "draw": All cells are filled with no winner (game over)
    - "ongoing": Game is still in progress
    
    Validation rules:
    - O cannot have more moves than X (X starts first)
    - X cannot have more than 1 more move than O
    - Both players cannot win at the same time
    
    Args:
        board: List of 3 strings (each 3 characters) representing the Tic-Tac-Toe board
    
    Returns:
        str: Game state ("win", "draw", "ongoing")
    
    Raises:
        ValueError: If the board has invalid turn order or impossible winning state
    """
    if count_player_moves(board, 'O') > count_player_moves(board, 'X'):
        raise ValueError('Wrong turn order: O started')
    if count_player_moves(board, 'X') - count_player_moves(board, 'O') > 1:
        raise ValueError('Wrong turn order: X went twice')
    if is_player_winner(board, 'X') and is_player_winner(board, 'O'):
        raise ValueError('Impossible board: game should have ended after the game was won')
    if is_player_winner(board, 'X') or is_player_winner(board, 'O'):
        return 'win'
    if count_player_moves(board, 'X') + count_player_moves(board, 'O') == 9:
        return 'draw'
    return 'ongoing'

if __name__ == '__main__':
    print(gamestate(['OOX', '   ', '   ']))
