# We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

# Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

 

# Example 1:

# Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4] and group2 [2,3].

# Example 2:

# Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false

# Example 3:

# Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false

 

# Constraints:

#     1 <= n <= 2000
#     0 <= dislikes.length <= 104
#     dislikes[i].length == 2
#     1 <= dislikes[i][j] <= n
#     ai < bi
#     All the pairs of dislikes are unique.

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        def helper(id,color):
            color_table[id] = color
            
            for other in dislike_table[id]:
                if color_table[other] == color:
                    return False
                
                if color_table[other] == NOT_COLORED and not helper(other,-color):
                    return False
            return True
    
        if n == 1 or len(dislikes) == 0:
            return True
        NOT_COLORED, BLUE, GREEN = 0,1,-1

        color_table = [0] * (n+1)

        dislike_table = defaultdict(list)
        for pair in dislikes:
            dislike_table[pair[1]].append(pair[0])
            dislike_table[pair[0]].append(pair[1])

        for i in range(1,n+1):
            if color_table[i] == NOT_COLORED and not helper(i,BLUE):
                return False
        return True
        
# Time complexity  O(N + E)

# Space complexity is O(N + E)