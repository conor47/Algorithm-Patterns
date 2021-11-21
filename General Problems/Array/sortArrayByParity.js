// Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

// Return any array that satisfies this condition.

// Example 1:

// Input: nums = [3,1,2,4]
// Output: [2,4,3,1]
// Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

// Example 2:

// Input: nums = [0]
// Output: [0]

// Constraints:

//     1 <= nums.length <= 5000
//     0 <= nums[i] <= 5000

const sortArrayByParity = function (nums) {
  if (nums.length <= 1) {
    return nums;
  }

  let index = 0;
  let i = 0;
  while (i < nums.length) {
    if (nums[i] % 2 === 0) {
      [nums[index], nums[i]] = [nums[i], nums[index]];
      index += 1;
    }
    i += 1;
  }
  return nums;
};

// Time complexity is O(N)

// Space complexity is O(1)
