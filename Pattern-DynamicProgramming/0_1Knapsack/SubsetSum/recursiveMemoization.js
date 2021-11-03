// Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given number ‘S’.
// Example 1:#

// Input: {1, 2, 3, 7}, S=6
// Output: True
// The given set has a subset whose sum is '6': {1, 2, 3}

// Example 2:#

// Input: {1, 2, 7, 1, 5}, S=10
// Output: True
// The given set has a subset whose sum is '10': {1, 2, 7}

// Example 3:#

// Input: {1, 3, 4, 8}, S=6
// Output: False
// The given set does not have any subset whose sum is equal to '6'.

const canPartition = function (num, sum) {
  if (num.length <= 0) return false;
  let dp = [];
  return canPartitionRecursive(num, sum, 0, dp);
};

const canPartitionRecursive = function (num, sum, currentIndex, dp) {
  if (sum === 0) return true;
  if (currentIndex >= num.length || num.length <= 0) return false;

  dp[currentIndex] = dp[currentIndex] || [];

  if (typeof dp[currentIndex][sum] !== 'undefined') {
    return dp[currentIndex][sum];
  }

  let foundPartition =
    canPartitionRecursive(num, sum, currentIndex + 1, dp) ||
    canPartitionRecursive(num, sum - num[currentIndex], currentIndex + 1, dp);

  dp[currentIndex][sum] = foundPartition;
  return foundPartition;
};

console.log(`Can partitioning be done: ---> ${canPartition([1, 2, 3, 4], 6)}`);
console.log(
  `Can partitioning be done: ---> ${canPartition([1, 2, 7, 1, 5], 10)}`
);
console.log(`Can partitioning be done: ---> ${canPartition([1, 3, 4, 8], 6)}`);
console.log(`Can partitioning be done: ---> ${canPartition([1, 3, 4, 8], 12)}`);
