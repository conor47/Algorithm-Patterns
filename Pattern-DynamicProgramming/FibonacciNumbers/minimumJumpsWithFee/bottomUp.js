const findMinFee = function (fee) {
  const dp = Array(fee.length + 1).fill(0);

  dp[0] = 0;
  dp[1] = fee[0];
  dp[2] = fee[0];

  for (let i = 2; i < fee.length; i++) {
    dp[i + 1] = Math.min(
      fee[i] + dp[i],
      fee[i - 1] + dp[i - 1],
      fee[i - 2] + dp[i - 2]
    );
  }

  return dp[fee.length];
};

console.log(`Minimum fee needed: ---> ${findMinFee([1, 2, 5, 2, 1, 2])}`);
console.log(`Minimum fee needed: ---> ${findMinFee([2, 3, 4, 5])}`);
