const findMaxSteal = function (wealth) {
  const recursive = function (wealth, index) {
    if (index >= wealth.length) {
      return 0;
    }

    let current = wealth[index] + recursive(wealth, index + 2);
    let skip = recursive(wealth, index + 1);

    return Math.max(current, skip);
  };
  return recursive(wealth, 0);
};

console.log(`Maximum stealing: ---> ${findMaxSteal([2, 5, 1, 3, 6, 2, 4])}`);
console.log(`Maximum stealing: ---> ${findMaxSteal([2, 10, 14, 8, 1])}`);

// Time complexity is O(2^n)

// Space complexity is O(n)
