// Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.
// Example 1:#

// Input: {1, 1, 2, 3}, S=4
// Output: 3
// The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
// Note that we have two similar sets {1, 3}, because we have two '1' in our input.

// Example 2:#

// Input: {1, 2, 7, 1, 5}, S=9
// Output: 3
// The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}

const countSubsets = function (num, sum) {
  let findSubsetsRecursive = function (num, currentIndex, sum, total) {
    if (sum === 0) return 1;

    if (currentIndex === num.length) return 0;

    let sum1 = 0;
    if (num[currentIndex] <= sum) {
      sum1 = findSubsetsRecursive(
        num,
        currentIndex + 1,
        sum - num[currentIndex]
      );
    }

    let sum2 = findSubsetsRecursive(num, currentIndex + 1, sum, total);

    return sum1 + sum2;
  };
  return findSubsetsRecursive(num, 0, sum, 0);
};

// Time complexity is O(2^N)

// Space complexity is O(n)

console.log(`Count of subset sum is: ---> ${countSubsets([1, 1, 2, 3], 4)}`);
console.log(`Count of subset sum is: ---> ${countSubsets([1, 2, 7, 1, 5], 9)}`);
