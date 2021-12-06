# We have n chips, where the position of the ith chip is position[i].

# We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:

#     position[i] + 2 or position[i] - 2 with cost = 0.
#     position[i] + 1 or position[i] - 1 with cost = 1.

# Return the minimum cost needed to move all the chips to the same position.

# Brute force solution

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        m = float('inf')
        for i in range(len(position)):
            total = 0
            for j in range(len(position)):
                if j != i:
                    if (position[j] + position[i]) % 2 == 0:
                        continue
                    else:
                        total +=1
            m = min(m,total)
        return m

# Time complexity is O(N^2)

# Space complexity is O(1)

# More efficient solution based on the intuition that any chip can be reduced to the curretn position or 1 away depending on whether they are
# an even number of positions away or odd. From there its a matter of moving the smaller pile onto the bigger pile since this gives the 
# smallest cost.

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = 0
        odd = 0
        for i in position:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(even,odd)

# Time complexity is O(N)

# Space complexity is O(1)