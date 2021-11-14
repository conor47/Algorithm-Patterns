// Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

// It is guaranteed that the answer will fit in a 32-bit integer.

// A subarray is a contiguous subsequence of the array.

// Example 1:

// Input: nums = [2,3,-2,4]
// Output: 6
// Explanation: [2,3] has the largest product 6.

// Example 2:

// Input: nums = [-2,0,-1]
// Output: 0
// Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

const maxProduct = function (nums) {
  if (nums.length === 1) return nums;
  let max = 0;
  for (let i = 0; i < nums.length; i++) {
    let current = 1;
    for (let j = i; j < nums.length; j++) {
      current *= nums[j];
      max = Math.max(max, current);
    }
  }
  return max;
};

// Time complexity is O(N^2)

// Space complexity is O(1)

// variation of Kadanes algorithm

var maxProductV2 = function (nums) {
  if (nums.length === 0) return 0;

  let maxSoFar = nums[0];
  let minSoFar = nums[0];
  let result = maxSoFar;
  for (let i = 1; i < nums.length; i++) {
    let cur = nums[i];
    tempMax = Math.max(cur, maxSoFar * cur, minSoFar * cur);
    minSoFar = Math.min(cur, maxSoFar * cur, minSoFar * cur);
    maxSoFar = tempMax;

    result = Math.max(result, maxSoFar);
  }
  return result;
};

// Time complexity is O(N)

// Space complexity is O(1)
