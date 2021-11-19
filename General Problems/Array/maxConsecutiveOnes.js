// Given a binary array nums, return the maximum number of consecutive 1's in the array.

// Example 1:

// Input: nums = [1,1,0,1,1,1]
// Output: 3
// Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

// Example 2:

// Input: nums = [1,0,1,1,0,1]
// Output: 2

const findMaxConsecutiveOnes = function (nums) {
  let max = 0;
  let start = 0;
  let end = 0;
  while (end < nums.length) {
    if (nums[end] === 1) {
      max = Math.max(max, end - start + 1);
      end += 1;
    } else {
      start = end + 1;
      end += 1;
    }
  }
  return max;
};

// Time complexity is O(N) where N is the lenght of nums

// Space complexity is O(1)

// alternative solution using a single pointer. Same time and space complexity

const findMaxConsecutive = function (nums) {
  let max = 0;
  let count = 0;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === 1) {
      count += 1;
    } else {
      max = Math.max(count, max);
      count = 0;
    }
  }
  return Math.max(max, count);
};
