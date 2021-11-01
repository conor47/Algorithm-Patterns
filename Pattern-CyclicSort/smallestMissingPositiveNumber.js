// Given an unsorted array containing numbers, find the smallest missing positive number in it.

// Example 1:

// Input: [-3, 1, 5, 4, 2]
// Output: 3
// Explanation: The smallest missing positive number is '3'

// Example 2:

// Input: [3, -2, 0, 1, 2]
// Output: 4

// Example 3:

// Input: [3, 2, 5, 1]
// Output: 4

const find_first_smallest_missing_positive = function (nums) {
  let i = 0;
  let n = nums.length;

  while (i < n) {
    let j = nums[i] - 1;
    if (nums[i] > 0 && nums[i] <= n && nums[i] !== nums[j]) {
      [nums[i], nums[j]] = [nums[j], nums[i]];
    } else {
      i += 1;
    }
  }

  for (i = 0; i < n; i++) {
    if (nums[i] !== i + 1) {
      return i + 1;
    }
  }
  return n + 1;
};

console.log(find_first_smallest_missing_positive([-3, 1, 5, 4, 2]));
console.log(find_first_smallest_missing_positive([3, -2, 0, 1, 2]));
console.log(find_first_smallest_missing_positive([3, 2, 5, 1]));
