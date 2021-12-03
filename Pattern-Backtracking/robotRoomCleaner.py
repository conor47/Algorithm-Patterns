# You are controlling a robot that is located somewhere in a room. The room is modeled as an m x n binary grid where 0 represents a wall and 1 represents an empty slot.

# The robot starts at an unknown location in the root that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API Robot.

# You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.

# When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.

# Design an algorithm to clean the entire room using the following APIs:

# interface Robot {
#   // returns true if next cell is open and robot moves into the cell.
#   // returns false if next cell is obstacle and robot stays on the current cell.
#   boolean move();

#   // Robot will stay on the same cell after calling turnLeft/turnRight.
#   // Each turn will be 90 degrees.
#   void turnLeft();
#   void turnRight();

#   // Clean the current cell.
#   void clean();
# }

# Note that the initial direction of the robot will be facing up. You can assume all four edges of the grid are all surrounded by a wall.

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def goBack():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        def solve(cell= (0,0), dir=0):
            visited.add(cell)
            robot.clean()
            
            for i in range(4):
                new_dir = (dir + i)%4
                new_cell = (cell[0] + directions[new_dir][0], cell[1] + directions[new_dir][1])
                
                if new_cell not in visited and robot.move():
                    solve(new_cell,new_dir)
                    goBack()
                robot.turnRight()
        
                
        visited = set()        
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        solve()

# Time complexity is O(N - M) Where N are the valid cells and M are the Obstacles. The time complexity is realy O 4(N - M) which simplifies 
# to O(N - M)

# Space complexity is O(N - M) for the visited set 