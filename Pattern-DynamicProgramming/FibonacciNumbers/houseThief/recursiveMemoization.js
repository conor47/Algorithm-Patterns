const findMaxSteal = function (wealth) {
  const dp = [];
  const recursive = function (wealth, index) {
    if (index >= wealth.length) {
      return 0;
    }

    if (typeof dp[index] === 'undefined') {
      let current = wealth[index] + recursive(wealth, index + 2);
      let skip = recursive(wealth, index + 1);

      dp[index] = Math.max(current, skip);
    }
    return dp[index];
  };
  return recursive(wealth, 0);
};

// Time complexity is O(n)

// Space complexity is O(n)

console.log(`Maximum stealing: ---> ${findMaxSteal([2, 5, 1, 3, 6, 2, 4])}`);
console.log(`Maximum stealing: ---> ${findMaxSteal([2, 10, 14, 8, 1])}`);
