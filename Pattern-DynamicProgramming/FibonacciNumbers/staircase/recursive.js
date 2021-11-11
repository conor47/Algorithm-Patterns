// Given a stair with ‘n’ steps, implement a method to count how many possible ways are there to reach the top of the staircase, given that, at every step you can either take 1 step, 2 steps, or 3 steps.

// Example 1:

// Number of stairs (n) : 3
// Number of ways = 4
// Explanation: Following are the four ways we can climb : {1,1,1}, {1,2}, {2,1}, {3}

// Example 2:

// Number of stairs (n) : 4
// Number of ways = 7
// Explanation: Following are the seven ways we can climb : {1,1,1,1}, {1,1,2}, {1,2,1}, {2,1,1},
// {2,2}, {1,3}, {3,1}

const CountWays = function (n) {
  if (n < 2) return 1;
  if (n == 2) return 2;

  return CountWays(n - 1) + CountWays(n - 2) + CountWays(n - 3);
};

// Time complexity is O(3^n) since we are making three recursive calls in the same function

// Space complexity is O(N) for the recursion stack

console.log(`Number of ways: ---> ${CountWays(3)}`);
console.log(`Number of ways: ---> ${CountWays(4)}`);
console.log(`Number of ways: ---> ${CountWays(5)}`);
