# Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:
# 
    # Players take turns placing characters into empty squares ' '.
    # The first player A always places 'X' characters, while the second player B always places 'O' characters.
    # 'X' and 'O' characters are always placed into empty squares, never on filled ones.
    # The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
    # The game also ends if all squares are non-empty.
    # No more moves can be played if the game is over.
# 
# Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".
# 
# You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        # n stands for the size of the board, n = 3 for the current game.
        n = 3

        # use rows and cols to record the value on each row and each column.
        # diag1 and diag2 to record value on diagonal or anti-diagonal.
        rows, cols = [0] * n, [0] * n
        diag = anti_diag = 0
        
        # Two players having value of 1 and -1, player_1 with value = 1 places first.
        player = 1
        
        for row, col in moves:
            
            # Update the row value and column value.
            rows[row] += player
            cols[col] += player
            
            # If this move is placed on diagonal or anti-diagonal, 
            # we shall update the relative value as well.
            if row == col:            
                diag += player
            if row + col == n - 1:
                anti_diag += player
                
            # check if this move meets any of the winning conditions.
            if any(abs(line) == n for line in (rows[row], cols[col], diag, anti_diag)):
                return "A" if player == 1 else "B"
        
            # If no one wins so far, change to the other player alternatively. 
            # That is from 1 to -1, from -1 to 1.
            player *= -1
            
        # If all moves are completed and there is still no result, we shall check if 
        # the grid is full or not. If so, the game ends with draw, otherwise pending.
        return "Draw" if len(moves) == n * n else "Pending"   

# Time complexity is O(M) where N is the number of moves

# Space complexity is O(N) where N is the size of the board