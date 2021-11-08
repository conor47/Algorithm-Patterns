// Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack that has a capacity ‘C’. The goal is to get the maximum profit from the items in the knapsack. The only difference between the 0/1 Knapsack problem and this problem is that we are allowed to use an unlimited quantity of an item.

let solveKnapsack = function (profits, weights, capacity) {
  let recursiveSearch = function (profits, weights, currentIndex, capacity) {
    if (
      capacity === 0 ||
      currentIndex >= profits.length ||
      weights.length !== profits.length ||
      profits.length === 0
    )
      return 0;

    // take the current item
    let profit1 = 0;
    if (capacity >= weights[currentIndex]) {
      profit1 +=
        profits[currentIndex] +
        recursiveSearch(
          profits,
          weights,
          currentIndex,
          capacity - weights[currentIndex]
        );
    }

    let profit2 = recursiveSearch(profits, weights, currentIndex + 1, capacity);

    return Math.max(profit1, profit2);

    // skip the current item
  };
  return recursiveSearch(profits, weights, 0, capacity);
};

// Time complexity is O(2^(N+C)) where N is the total number of items

// The space complexity is O(N + C)

var profits = [15, 50, 60, 90];
var weights = [1, 3, 4, 5];
console.log(
  `Total knapsack profit: ---> ${solveKnapsack(profits, weights, 8)}`
);
