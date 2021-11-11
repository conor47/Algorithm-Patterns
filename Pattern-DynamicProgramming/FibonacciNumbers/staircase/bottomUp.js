const CountWays = function (n) {
  if (n < 2) return 1;
  if (n === 2) return 2;

  const dp = [1, 1, 2];
  for (let i = 3; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
  }
  return dp[n];
};

// Time complexity is O(N).

// Space complexity is O(N)

// Solution which optimises space complexity. Relies on that fact that we need only store the last 3 values at any one point to calculate the
// next value

const CountWaysV2 = function (n) {
  if (n < 2) return 1;
  if (n == 2) return 2;
  let n1 = 1,
    n2 = 1,
    n3 = 2,
    temp;
  for (let i = 3; i <= n; i++) {
    temp = n1 + n2 + n3;
    n1 = n2;
    n2 = n3;
    n3 = temp;
  }
  return n3;
};

//   Time complexity is O(N)

// Space complexity is O(1)

console.log(`Number of ways: ---> ${CountWays(3)}`);
console.log(`Number of ways: ---> ${CountWays(4)}`);
console.log(`Number of ways: ---> ${CountWays(5)}`);
