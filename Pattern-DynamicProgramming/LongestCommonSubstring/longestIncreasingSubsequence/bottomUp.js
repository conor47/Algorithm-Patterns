const findLISLength = function (nums) {
  let n = nums.length;
  const dp = Array(n).fill(0);
  dp[0] = 1;

  let maxLength = 1;
  for (let i = 1; i < n; i++) {
    dp[i] = 1;
    for (let j = 0; j < i; j++) {
      if (nums[i] > nums[j] && dp[i] <= dp[j]) {
        dp[i] = dp[j] + 1;
        maxLength = Math.max(dp[i], maxLength);
      }
    }
  }
  return maxLength;
};

// Time complexity is O(N^2)

// Space complexity is O(N)

console.log(
  `Length of Longest Increasing Subsequence: ---> ${findLISLength([
    4, 2, 3, 6, 10, 1, 12,
  ])}`
);
console.log(
  `Length of Longest Increasing Subsequence: ---> ${findLISLength([
    -4, 10, 3, 7, 15,
  ])}`
);
