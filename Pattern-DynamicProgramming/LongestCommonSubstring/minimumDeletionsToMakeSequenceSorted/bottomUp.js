const findMinimumDeletions = function (nums) {
  return nums.length - findLISLength(nums);
};

const findLISLength = function (nums) {
  const dp = Array(nums.length).fill(0);

  dp[0] = 1;
  let max = 1;

  for (let i = 1; i < nums.length; i++) {
    dp[i] = 1;

    for (let j = 0; j < i; j++) {
      if (nums[i] > nums[j] && dp[i] <= dp[j]) {
        dp[i] = dp[j] + 1;
        max = Math.max(max, dp[i]);
      }
    }
  }
  return max;
};

// Time complexity is O(n^2)

// The space complexity is O(n)

console.log(
  `Minimum deletion needed: ---> ${findMinimumDeletions([
    4, 2, 3, 6, 10, 1, 12,
  ])}`
);
console.log(
  `Minimum deletion needed: ---> ${findMinimumDeletions([-4, 10, 3, 7, 15])}`
);
console.log(
  `Minimum deletion needed: ---> ${findMinimumDeletions([3, 2, 1, 0])}`
);
