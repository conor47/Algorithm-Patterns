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
  const memo = [];
  function recursive(n) {
    if (n < 2) return 1;
    if (n === 2) return 2;

    if (typeof memo[n] === 'undefined') {
      memo[n] = recursive(n - 1) + recursive(n - 2) + recursive(n - 3);
    }
    return memo[n];
  }
  return recursive(n);
};

// Time complexity is O(N) since we will have no more than n + 1 subproblems to calculate

// Space complexity is O(N) for the recursion stack

console.log(`Number of ways: ---> ${CountWays(3)}`);
console.log(`Number of ways: ---> ${CountWays(4)}`);
console.log(`Number of ways: ---> ${CountWays(5)}`);
