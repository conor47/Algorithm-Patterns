// Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack that has a capacity ‘C’. The goal is to get the maximum profit from the items in the knapsack. The only difference between the 0/1 Knapsack problem and this problem is that we are allowed to use an unlimited quantity of an item.

let solveKnapsack = function (profits, weights, capacity) {
  let dp = [];
  let recursiveSearch = function (profits, weights, currentIndex, capacity) {
    if (
      capacity === 0 ||
      currentIndex >= profits.length ||
      weights.length !== profits.length ||
      profits.length === 0
    )
      return 0;

    dp[currentIndex] = dp[currentIndex] || [];

    // take the current item
    if (typeof dp[currentIndex][capacity] === 'undefined') {
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

      let profit2 = recursiveSearch(
        profits,
        weights,
        currentIndex + 1,
        capacity
      );

      dp[currentIndex][capacity] = Math.max(profit1, profit2);
    }

    return dp[currentIndex][capacity];
  };
  return recursiveSearch(profits, weights, 0, capacity);
};

// Time complexity is O(N * C) since we will have no more than N * C subproblems. N is the number of items and C is the capacity

// The space complexity is O(N * C) to store the memoization array. We will also use O(N) for the recursion call stack but O(N*C + N) is
// asymptotically equivalent to O(N * C)

var profits = [15, 50, 60, 90];
var weights = [1, 3, 4, 5];
console.log(
  `Total knapsack profit: ---> ${solveKnapsack(profits, weights, 8)}`
);
