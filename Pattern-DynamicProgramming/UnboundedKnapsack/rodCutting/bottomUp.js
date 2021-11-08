const solveRodCutting = function (lengths, prices, n) {
  if (lengths.length === 0 || lengths.length !== prices.length || n <= 0)
    return 0;

  let len = lengths.length;

  let dp = Array(len)
    .fill(0)
    .map(() => Array(n + 1).fill(0));

  for (let i = 0; i < len; i++) {
    dp[i][0] = 0;
  }

  for (let i = 1; i <= n; i++) {
    if (lengths[0] <= i) {
      dp[0][i] = prices[0];
    }
  }

  for (let i = 1; i < len; i++) {
    for (let j = 1; j <= n; j++) {
      let profit1 = 0;
      let profit2 = 0;
      if (lengths[i] <= j) {
        profit1 = prices[i] + dp[i][j - lengths[i]];
      }
      profit2 = dp[i - 1][j];
      dp[i][j] = Math.max(profit1, profit2);
    }
  }

  return dp[len - 1][n];
};

// Time and space complexity are O(N * L) where N is the number of lengths and L is the
// length of the given rod

const lengths = [1, 2, 3, 4, 5];
const prices = [2, 6, 7, 10, 13];
console.log(`Maximum profit: ---> ${solveRodCutting(lengths, prices, 5)}`);
