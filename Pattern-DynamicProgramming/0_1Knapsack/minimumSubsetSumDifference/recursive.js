// Given a set of positive numbers, partition the set into two subsets with a minimum difference between their subset sums.
// Example 1:#

// Input: {1, 2, 3, 9}
// Output: 3
// Explanation: We can partition the given set into two subsets where the minimum absolute difference
// between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.

// Example 2:#

// Input: {1, 2, 7, 1, 5}
// Output: 0
// Explanation: We can partition the given set into two subsets where the minimum absolute difference
// between the sum of numbers is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.

// Example 3:#

// Input: {1, 3, 100, 4}
// Output: 92
// Explanation: We can partition the given set into two subsets where the minimum absolute difference
// between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.

let canPartition = function (num) {
  function canPartitionRecursive(num, currentIndex, sum1, sum2) {
    if (currentIndex === num.length) return Math.abs(sum1 - sum2);

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

    return Math.min(diff1, diff2);
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
