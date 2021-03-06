// Given an infinite supply of ānā coin denominations and a total money amount, we are asked to find the total number of distinct ways to make up that amount.

// Example:

// Denominations: {1,2,3}
// Total amount: 5
// Output: 5
// Explanation: There are five ways to make the change for '5', here are those ways:
//   1. {1,1,1,1,1}
//   2. {1,1,1,2}
//   3. {1,2,2}
//   4. {1,1,3}
//   5. {2,3}

let countChange = function (denominations, total) {
  let dp = [];
  let recursiveSearch = function (denominations, currentIndex, total) {
    if (currentIndex >= denominations.length || denominations.length === 0)
      return 0;

    if (currentIndex < denominations.length && total === 0) {
      return 1;
    }

    dp[currentIndex] = dp[currentIndex] || [];

    if (typeof dp[currentIndex][total] === 'undefined') {
      let val1 = 0;
      if (denominations[currentIndex] <= total) {
        val1 = recursiveSearch(
          denominations,
          currentIndex,
          total - denominations[currentIndex]
        );
      }

      let val2 = recursiveSearch(denominations, currentIndex + 1, total);

      dp[currentIndex][total] = val1 + val2;
    }
    return dp[currentIndex][total];
  };
  return recursiveSearch(denominations, 0, total);
};

// Time complexity is O(2^(N + T)) where T is the total

// Space complexity is O(N + T)

console.log(`Number of ways to make change: ---> ${countChange([1, 2, 3], 5)}`);
