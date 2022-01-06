# There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.

# The rules of the game are as follows:

#     Start at the 1st friend.
#     Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.
#     The last friend you counted leaves the circle and loses the game.
#     If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
#     Else, the last friend in the circle wins the game.

# Given the number of friends, n, and an integer k, return the winner of the game.

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(n)]
        i = 0
        while len(friends) > 1:
            i = (i + k -1) % (len(friends)) 
            friends.pop(i)
            i = (i) % len(friends)
        return friends[0] + 1
    
# Time complexity is O(N)

# Space complexity is O(N)