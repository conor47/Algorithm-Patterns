const findMaxSteal = function (wealth) {
  const dp = Array(wealth.length + 1).fill(0);

  dp[0] = 0;
  dp[1] = wealth[0];

  for (let i = 1; i < wealth.length; i++) {
    dp[i + 1] = Math.max(wealth[i] + dp[i - 1], dp[i]);
  }
  return dp[wealth.length];
};
