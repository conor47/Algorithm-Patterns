// Given a number sequence, find the increasing subsequence with the highest sum. Write a method that returns the highest sum.

// Example 1:

// Input: {4,1,2,6,10,1,12}
// Output: 32
// Explanation: The increaseing sequence is {4,6,10,12}.
// Please note the difference, as the LIS is {1,2,6,10,12} which has a sum of '31'.

// Example 2:

// Input: {-4,10,3,7,15}
// Output: 25
// Explanation: The increaseing sequences are {10, 15} and {3,7,15}.

const findMSIS = function (nums) {
  const dp = [];
  const recursive = function (nums, previousIndex, currentIndex, sum) {
    if (currentIndex >= nums.length) {
      return sum;
    }
    const key = `${currentIndex}-${previousIndex}-${sum}`;
    if (typeof dp[key] === 'undefined') {
      let c1 = sum;
      if (previousIndex === -1 || nums[currentIndex] > nums[previousIndex]) {
        c1 = recursive(
          nums,
          currentIndex,
          currentIndex + 1,
          sum + nums[currentIndex]
        );
      }

      let c2 = recursive(nums, previousIndex, currentIndex + 1, sum);
      dp[key] = Math.max(c1, c2);
    }
    return dp[key];
  };
  return recursive(nums, -1, 0, 0);
};

console.log(
  `Maximum Sum Increasing Subsequence is: ---> ${findMSIS([
    4, 1, 2, 6, 10, 1, 12,
  ])}`
);
console.log(
  `Maximum Sum Increasing Subsequence is: ---> ${findMSIS([-4, 10, 3, 7, 15])}`
);
