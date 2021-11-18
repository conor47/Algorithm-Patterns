// Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

// Note: You can only move either down or right at any point in time.

// Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
// Output: 7
// Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

// Example 2:

// Input: grid = [[1,2,3],[4,5,6]]
// Output: 12

// Constraints:

//     m == grid.length
//     n == grid[i].length
//     1 <= m, n <= 200
//     0 <= grid[i][j] <= 100

const minPathSum = function (grid) {
  if (grid.length === 0 || grid === null) return 0;

  const dp = Array(grid.length)
    .fill(0)
    .map(() => Array(grid[0].length).fill(0));

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      dp[i][j] += grid[i][j];
      if (i > 0 && j > 0) {
        dp[i][j] += Math.min(dp[i - 1][j], dp[i][j - 1]);
      } else if (i > 0) {
        dp[i][j] += dp[i - 1][j];
      } else if (j > 0) {
        dp[i][j] += dp[i][j - 1];
      }
    }
  }
  return dp[dp.length - 1][dp[0].length - 1];
};

// time complexity is O(N* M)

// space complexity is O(N * M)
