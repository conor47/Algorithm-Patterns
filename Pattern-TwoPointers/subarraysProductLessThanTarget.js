// Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.

// Example 1:

// Input: [2, 5, 3, 10], target=30
// Output: [2], [5], [2, 5], [3], [5, 3], [10]
// Explanation: There are six contiguous subarrays whose product is less than the target.

// Example 2:

// Input: [8, 2, 6, 5], target=50
// Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]
// Explanation: There are seven contiguous subarrays whose product is less than the target.

const Deque = require('collections/deque');

const find_subarrays = function (arr, target) {
  result = [];
  let product = 1;
  let left = 0;
  for (let right = 0; right < arr.length; right++) {
    product *= arr[right];
    while (product >= target && left <= arr.length) {
      product /= arr[left];
      left += 1;
    }

    let temp = new Deque();
    for (let i = right; i > left - 1; i--) {
      temp.unshift(arr[i]);
      result.push(temp.toArray());
    }
  }
  return result;
};

// Time complexity is O(N^3). Complexity for main loop managing sliding window is O(N) but creating sub arrays can take O(N^2) in
// worst case

// Space complexity
