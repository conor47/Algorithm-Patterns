const CountWays = function (n) {
  if (n === 0) {
    return 1;
  }
  if (n === 1) {
    return 1;
  }
  if (n === 2) {
    return 1;
  }
  if (n === 3) {
    return 2;
  }

  const dp = [1, 1, 1, 2];

  for (let i = 4; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 4];
  }
  return dp[n];
};

console.log(`Number of ways: ---> ${CountWays(4)}`);
console.log(`Number of ways: ---> ${CountWays(5)}`);
console.log(`Number of ways: ---> ${CountWays(6)}`);
