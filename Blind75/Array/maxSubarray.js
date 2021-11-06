// Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

// A subarray is a contiguous part of an array.

let maxSubArray = function (nums) {
  if (nums.length === 1) return nums[0];
  if (nums.length === 0) return 0;
  let currentSubarray = nums[0];
  let maxSubarray = nums[0];

  for (let i = 1; i < nums.length; i++) {
    currentSubarray = Math.max(nums[i], currentSubarray + nums[i]);
    maxSubarray = Math.max(maxSubarray, currentSubarray);
  }
  return maxSubarray;
};

// time complexity is O(n)

// space complexity is O(1)
