// Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

// You must implement a solution with a linear runtime complexity and use only constant extra space.

// Example 1:

// Input: nums = [2,2,3,2]
// Output: 3

// Example 2:

// Input: nums = [0,1,0,1,0,1,99]
// Output: 99

// Constraints:

//     1 <= nums.length <= 3 * 104
//     -231 <= nums[i] <= 231 - 1
//     Each element in nums appears exactly three times except for one element which appears once.

// Naieve solution. Time complexity is O(N) and space complexity is also O(N). Solves the question but does not meet the
// constant space constraint

var singleNumber = function (nums) {
  frequency = new Map();
  for (let num of nums) {
    if (frequency.has(num)) frequency.set(num, frequency.get(num) + 1);
    else frequency.set(num, 1);
  }

  for (let key of frequency.keys()) {
    if (frequency.get(key) === 1) return key;
  }
};

// Constant space solution
