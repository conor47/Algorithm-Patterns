# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].


# A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        seen = set() 
        q = [(0,0)]
        steps = 0
        while q:
            curLevel = len(q)
            for i in range(curLevel):
                
                row,col = q.pop(0)
                if row == x and col == y:
                    return steps
                for a,b in self.generateMoves(row,col):
                    if (a,b) not in seen:
                        q.append((a,b))
                        seen.add((a,b))
            steps += 1
              
        
    def generateMoves(self, row,col):
        for x,y in ((row+1,col+2), (row+2, col+1),(row+2, col-1),(row+1,col-2),(row-1,col+2),(row-2,col+1),(row-1,col-2),(row-2,col-1) ):
            yield(x,y)

# Time complexity is O(max(abs(x),abs(y))^2)

# Space complexity is O(max(abs(x),abs(y))^2)