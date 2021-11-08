let canPartition = function (num) {
  let dp = [];
  function canPartitionRecursive(num, currentIndex, sum1, sum2) {
    if (currentIndex === num.length) return Math.abs(sum1 - sum2);

    dp[currentIndex] = dp[currentIndex] || [];

    if (typeof dp[currentIndex][sum1] === 'undefined') {
      const diff1 = canPartitionRecursive(
        num,
        currentIndex + 1,
        sum1 + num[currentIndex],
        sum2
      );
      const diff2 = canPartitionRecursive(
        num,
        currentIndex + 1,
        sum1,
        sum2 + num[currentIndex]
      );

      dp[currentIndex][sum1] = Math.min(diff1, diff2);
    }

    return dp[currentIndex];
  }
  return canPartitionRecursive(num, 0, 0, 0);
};

// time complexity is O(2^n)
// space complexity is O(n) for the recursion stack

console.log(`Minimum subset difference is: ---> ${canPartition([1, 2, 3, 9])}`);
console.log(
  `Minimum subset difference is: ---> ${canPartition([1, 2, 7, 1, 5])}`
);
console.log(
  `Minimum subset difference is: ---> ${canPartition([1, 3, 100, 4])}`
);
