// Given a set of positive numbers (non zero) and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign. We need to find out total ways to assign symbols to make the sum of numbers equal to target ‘S’.
// Example 1:#

// Input: {1, 1, 2, 3}, S=1
// Output: 3
// Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}

// Example 2:#

// Input: {1, 2, 7, 1}, S=9
// Output: 2
// Explanation: The given set has '2' ways to make a sum of '9': {+1+2+7-1} & {-1+2+7+1}

var findTargetSubsets = function (num, sum) {
  let findSubsetsRecursive = function (num, currentIndex, sum) {
    if (sum === 0 && currentIndex === num.length) return 1;

    if (currentIndex === num.length) return 0;

    let sum1 = 0;

    sum1 = findSubsetsRecursive(num, currentIndex + 1, sum + num[currentIndex]);

    let sum2 = findSubsetsRecursive(
      num,
      currentIndex + 1,
      sum - num[currentIndex]
    );

    return sum1 + sum2;
  };
  return findSubsetsRecursive(num, 0, sum);
};

console.log(
  `Count of Target sum is: ---> ${findTargetSubsets([1, 1, 2, 3], 1)}`
);
console.log(
  `Count of Target sum is: ---> ${findTargetSubsets([1, 2, 7, 1], 9)}`
);

// Time complexity is O(2^n)

// Space complexity is O(N)
