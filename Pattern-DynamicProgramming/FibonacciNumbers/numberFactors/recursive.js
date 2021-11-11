// Given a number ‘n’, implement a method to count how many possible ways there are to express ‘n’ as the sum of 1, 3, or 4.

// Example 1:

// n : 4
// Number of ways = 4
// Explanation: Following are the four ways we can express 'n' : {1,1,1,1}, {1,3}, {3,1}, {4}

// Example 2:

// n : 5
// Number of ways = 6
// Explanation: Following are the six ways we can express 'n' : {1,1,1,1,1}, {1,1,3}, {1,3,1}, {3,1,1},
// {1,4}, {4,1}

const CountWays = function (n) {
  if (n === 0) {
    return 1;
  }
  if (n === 1) {
    return 1;
  }
  if (n === 2) {
    return 1;
  }
  if (n === 3) {
    return 2;
  }

  return CountWays(n - 1) + CountWays(n - 3) + CountWays(n - 4);
};

// Time complexity is O(3^N)

// Space complexity is O(N)

console.log(`Number of ways: ---> ${CountWays(4)}`);
console.log(`Number of ways: ---> ${CountWays(5)}`);
console.log(`Number of ways: ---> ${CountWays(6)}`);
