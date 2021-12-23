# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

# The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth. Let maxDepth be the maximum depth of any integer.

# The weight of an integer is maxDepth - (the depth of the integer) + 1.

# Return the sum of each integer in nestedList multiplied by its weight.

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        q = [l for l in nestedList]
        maxDepth = 0
        sumOfElements = 0
        sumOfProducts = 0
        depth = 1
        while q:
            maxDepth = max(maxDepth,depth)
            
            for i in range (len(q)):
                n = q.pop(0)
                if n.isInteger():
                    sumOfElements += n.getInteger()
                    sumOfProducts += n.getInteger() * depth
                else:
                    q.extend([i for i in n.getList()])
            depth += 1
        return (maxDepth + 1) * sumOfElements - sumOfProducts

# Time complexity is O(N) since each element is added and popped from the queue once

# Space complexity is O(N) since in the worst case all of the elements are at the same depth