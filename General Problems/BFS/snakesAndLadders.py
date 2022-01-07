# You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

# You start on square 1 of the board. In each move, starting from square curr, do the following:

#     Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
#         This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
#     If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
#     The game ends when you reach the square n2.

# A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 do not have a snake or ladder.

# Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

#     For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.

# Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.

class Solution(object):
    def snakesAndLadders(self, board):
        
        # flatten board into a 1D array
        board.reverse()
        arr = [0]
        for i, row in enumerate(board):
            if i % 2 == 0:
                arr += row
            else:
                arr += row[::-1]   
        
        NN = len(board)**2
        queue = [1]
        visited = set()
        moves = 0
        while queue:
            
            next_level = []
            while queue:
                
                square = queue.pop()
                if square == NN: 
                    return moves 
                
                # visit every dice role (1 to 6)
                for i in range(1, 7):
                    
                    # don't visit squares we already saw, don't visit a square past N*N
                    if square + i <= NN and square + i not in visited:
                        visited.add(square + i)
                        
                        # if next square is a snake/ladder, take it
                        if arr[square + i] != -1:
                            next_level.append(arr[square + i])
                        # otherwise go to the square (1 to 6) hops away
                        else:
                            next_level.append(square + i)
                                                
            queue = next_level
            moves = moves + 1
            
        return -1 

# Time complexity is O(N) where N is the number of cells in the grid. Each cell is visited at most once

# Space complexity is O(N)