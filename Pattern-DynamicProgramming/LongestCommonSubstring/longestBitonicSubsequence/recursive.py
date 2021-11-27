# Given a number sequence, find the length of its Longest Bitonic Subsequence (LBS). A subsequence is considered bitonic if it is monotonically increasing and then monotonically decreasing.

# Input: {4,2,3,6,10,1,12}
# Output: 5
# Explanation: The LBS is {2,3,6,10,1}.

# Example 2:

# Input: {4,2,5,9,7,6,10,3,1}
# Output: 7
# Explanation: The LBS is {4,5,9,7,6,3,1}.

def find_LBS_length(nums):
    maxLength = 0
    for i in range(len(nums)):
        longest1 = lis(nums,i,-1)
        longest2 = lisr(nums,i,-1)
        maxLength = max(maxLength, longest1 + longest2 - 1)
    return maxLength

def lis(nums,current,previous):
    if current == len(nums):
        return 0

    c1 = 0
    if previous == -1 or nums[current] < nums[previous]:
        c1 = 1 + lis(nums,current+1,current)
    
    c2 = lis(nums,current+1,previous)

    return max(c1,c2)

def lisr(nums,current,previous):
    if current < 0:
        return 0

    c1 = 0
    if previous == -1 or nums[current] < nums[previous]:
        c1 = 1 + lisr(nums,current-1,current)
    
    c2 = lisr(nums,current-1,previous)

    return max(c1,c2)

# Time complexity is O(2^N) where N is the length of the input array

# Space complexity is O(N) for the recursion stack

def main():
  print(find_LBS_length([4, 2, 3, 6, 10, 1, 12]))
  print(find_LBS_length([4, 2, 5, 9, 7, 6, 10, 3, 1]))


main()