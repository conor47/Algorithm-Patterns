// Given an infinite supply of ‘n’ coin denominations and a total money amount, we are asked to find the minimum number of coins needed to make up that amount.

// Example 1:

// Denominations: {1,2,3}
// Total amount: 5
// Output: 2
// Explanation: We need a minimum of two coins {2,3} to make a total of '5'

// Example 2:

// Denominations: {1,2,3}
// Total amount: 11
// Output: 4
// Explanation: We need a minimum of four coins {2,3,3,3} to make a total of '11'

let countChange = function (denominations, total) {
  let recursiveSearch = function (denominations, total, currentIndex) {
    if (total === 0) {
      return 0;
    }

    if (currentIndex >= denominations.length || denominations.length === 0) {
      return Number.MAX_VALUE;
    }

    let total1 = Number.MAX_VALUE;
    if (denominations[currentIndex] <= total) {
      let res = recursiveSearch(
        denominations,
        total - denominations[currentIndex],
        currentIndex
      );
      if (res !== Number.MAX_VALUE) {
        total1 = res + 1;
      }
    }

    let total2 = recursiveSearch(denominations, total, currentIndex + 1);
    return Math.min(total1, total2);
  };
  let result = recursiveSearch(denominations, total, 0);
  return result === Number.MAX_VALUE ? -1 : result;
};

console.log(`Number of ways to make change: ---> ${countChange([1, 2, 3], 5)}`);
console.log(
  `Number of ways to make change: ---> ${countChange([1, 2, 3], 11)}`
);
console.log(`Number of ways to make change: ---> ${countChange([1, 2, 3], 7)}`);
console.log(`Number of ways to make change: ---> ${countChange([3, 5], 7)}`);
