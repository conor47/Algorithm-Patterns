// Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

// You must write an algorithm that runs in O(n) time and without using the division operation.

// Example 1:

// Input: nums = [1,2,3,4]
// Output: [24,12,8,6]

// Example 2:

// Input: nums = [-1,1,0,-3,3]
// Output: [0,0,9,0,0]

let productExceptSelf = function (nums) {
  if (nums.length === 0) return [];
  let length = nums.length;
  let result = [];

  let left = Array(length).fill(0);
  let right = Array(length).fill(0);
  left[0] = 1;
  right[length - 1] = 1;

  for (let i = 1; i < length; i++) {
    left[i] = left[i - 1] * nums[i - 1];
  }

  for (let i = length - 2; i >= 0; i--) {
    right[i] = right[i + 1] * nums[i + 1];
  }

  for (let i = 0; i < nums.length; i++) {
    result[i] = left[i] * right[i];
  }
  return result;
};

// time complextiy is O(n)

// space complexity is O(n)
