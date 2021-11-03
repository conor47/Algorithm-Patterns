// Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.
// Example 1: #

// Input: {1, 2, 3, 4}
// Output: True
// Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}

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
  for (let i = 0; i < num.length; i++) sum += num[i];

  if (sum % 2 !== 0) return false;
  return canPartitionRecursive(num, sum / 2, 0);
};

let canPartitionRecursive = function (num, sum, currentIndex) {
  if (sum === 0) return true;
  if (num.length === 0 || currentIndex >= num.length) return false;

  if (num[currentIndex] <= sum) {
    if (canPartitionRecursive(num, sum - num[currentIndex], currentIndex + 1))
      return true;
  }

  return canPartitionRecursive(num, sum, currentIndex + 1);
};

// Time complextiy of this algorithm is O(2^n)

// Space complexity is O(n) for the recrusion stack

console.log(`Can partitioning be done: ---> ${canPartition([1, 2, 3, 4])}`);
console.log(`Can partitioning be done: ---> ${canPartition([1, 1, 3, 4, 7])}`);
console.log(`Can partitioning be done: ---> ${canPartition([2, 3, 4, 6])}`);
