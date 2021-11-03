// Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C.’ Each item can only be selected once, which means either we put an item in the knapsack or we skip it.

let solveKnapsack = function (profits, weights, capacity) {
  function knapsackRecursive(profits, weights, capacity, currentIndex) {
    // base checks
    if (capacity <= 0 || currentIndex >= profits.length) return 0;

    let profit1 = 0;
    if (weights[currentIndex] <= capacity) {
      profit1 =
        profits[currentIndex] +
        knapsackRecursive(
          profits,
          weights,
          capacity - weights[currentIndex],
          currentIndex + 1
        );
    }

    const profit2 = knapsackRecursive(
      profits,
      weights,
      capacity,
      currentIndex + 1
    );

    return Math.max(profit1, profit2);
  }

  return knapsackRecursive(profits, weights, capacity, 0);
};

// Time complexity of this solution is O(2^n) since we are making 31 recursive calls. Calculated through 2^n + 2^n - 1 which is
// asymptotically equivalent to 2^n

// Space complexity is O(n) since the recursive algorithm works in a depth first fashion.

var profits = [1, 6, 10, 16];
var weights = [1, 2, 3, 5];
console.log(
  `Total knapsack profit: ---> ${solveKnapsack(profits, weights, 7)}`
);
console.log(
  `Total knapsack profit: ---> ${solveKnapsack(profits, weights, 6)}`
);
