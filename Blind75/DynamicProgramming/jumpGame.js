// You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

// Return true if you can reach the last index, or false otherwise.

// Example 1:

// Input: nums = [2,3,1,1,4]
// Output: true
// Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

// Example 2:

// Input: nums = [3,2,1,0,4]
// Output: false
// Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

// Constraints:

//     1 <= nums.length <= 104
//     0 <= nums[i] <= 105

var canJump = function (nums) {
  let minimumJumps = nums.length - 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    if (i + nums[i] >= minimumJumps) {
      minimumJumps = i;
    }
  }
  return minimumJumps === 0;
};

// Time complexity is O(N)

// Space complexity is O(1)

// back tracking solution

const canJumpV2 = function (nums) {
  return canJumpFromPosition(0, nums);
};

const canJumpFromPosition = function (index, nums) {
  if (index === nums.length - 1) {
    return true;
  }

  let maxJump = Math.min(index + nums[index], nums.length - 1);
  for (let nextPosition = index + 1; nextPosition <= maxJump; nextPosition++) {
    if (canJumpFromPosition(nextPosition, nums)) {
      return true;
    }
  }
  return false;
};
