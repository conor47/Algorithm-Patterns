// Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.
// Example 1: #

// Output: True
// Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}

// Input: {1, 2, 3, 4}
// Example 2: #

// Input: {1, 1, 3, 4, 7}
// Output: True
// Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}

// Example 3: #

// Input: {2, 3, 4, 6}
// Output: False
// Explanation: The given set cannot be partitioned into two subsets with equal sum.

let canPartition = function (num) {
  let sum = 0;
  //   find sum of all values in num
  for (let i = 0; i < num.length; i++) {
    sum += num[i];
  }

  if (sum % 2 !== 0) return false;

  let target = sum / 2;

  //   build out grid
  let dp = Array(num.length)
    .fill(false)
    .map(() => Array(target + 1).fill(false));

  //   fill first column with true. For a target of 0 we can always find a partition
  for (let i = 0; i < num.length; i++) {
    dp[i][0] = true;
  }

  for (let i = 1; i <= target; i++) {
    dp[0][i] = num[0] === i;
  }

  //   iterate over rows
  for (let i = 1; i < num.length; i++) {
    //   iterate over columns
    for (let j = 1; j <= target; j++) {
      if (dp[i - 1][j]) {
        dp[i][j] = dp[i - 1][j];
      } else if (j >= num[i]) {
        dp[i][j] = dp[i - 1][j - num[i]];
      }
    }
  }

  return dp[num.length - 1][target];
};

console.log(`Can partitioning be done: ---> ${canPartition([1, 2, 3, 4])}`);
console.log(`Can partitioning be done: ---> ${canPartition([1, 1, 3, 4, 7])}`);
console.log(`Can partitioning be done: ---> ${canPartition([2, 3, 4, 6])}`);
