// Given a set of positive numbers (non zero) and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign. We need to find out total ways to assign symbols to make the sum of numbers equal to target ‘S’.
// Example 1:#

// Input: {1, 1, 2, 3}, S=1
// Output: 3
// Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}

// Example 2:#

// Input: {1, 2, 7, 1}, S=9
// Output: 2
// Explanation: The given set has '2' ways to make a sum of '9': {+1+2+7-1} & {-1+2+7+1}

var findTargetSumWays = function (num, sum) {
  let dp = [];
  let findSubsetsRecursive = function (num, currentIndex, sum) {
    if (sum === 0 && currentIndex === num.length) return 1;

    if (currentIndex === num.length) return 0;

    dp[currentIndex] = dp[currentIndex] || [];

    let sum1 = 0;
    if (typeof dp[currentIndex][sum] === 'undefined') {
      sum1 = findSubsetsRecursive(
        num,
        currentIndex + 1,
        sum + num[currentIndex]
      );

      let sum2 = findSubsetsRecursive(
        num,
        currentIndex + 1,
        sum - num[currentIndex]
      );

      dp[currentIndex][sum] = sum1 + sum2;
    }
    return dp[currentIndex][sum];
  };
  return findSubsetsRecursive(num, 0, sum);
};

//   Time complexity is O(N * S)

// Space complexity is O(N * S)
