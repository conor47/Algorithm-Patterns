# ou are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

# The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

# Return the sum of each integer in nestedList multiplied by its depth.

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        res = 0
        q = [(l,1) for l in nestedList]
        while q:
            val,depth = q.pop(0)
            if val.isInteger():
                res += val.getInteger() * depth
            else:
                for i in val.getList():
                    q.append((i,depth+1))
        return res

# Time complexity is O(N) where N is the number of total items in the nested list 

# Space complexity is O(N) as in the worst case all the elements are in a single layer and are all inserted into the queue
