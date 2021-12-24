# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start,end):
            if start == end:
                if tuple(nums) not in memo:
                    ans.append(nums[:])
                    memo.add(tuple(nums))
            for i in range(start,end):
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(start+1,end)
                nums[i], nums[start] = nums[start], nums[i]
        memo = set()
        ans = []
        backtrack(0,len(nums))
        return ans

# Time complexity seen online

# Space complexity is O(N!)

# More efficient solution using a hashtable / counter. Uses O(N) space

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(comb,counter):
            if len(comb) == len(nums):
                ans.append(comb[:])
                return
            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    backtrack(comb,counter)
                    comb.pop()
                    counter[num] += 1
        ans = []
        backtrack([], Counter(nums))
        return ans