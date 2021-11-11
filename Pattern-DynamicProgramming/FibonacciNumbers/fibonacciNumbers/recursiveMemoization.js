// Write a function to calculate the nth Fibonacci number.

const calcFibonacci = function (n) {
  const memo = [];

  function fibonacci(n) {
    if (n < 2) {
      return n;
    }

    if (memo[n]) {
      return memo[n];
    }

    memo[n] = fibonacci(n - 1) + fibonacci(n - 2);
    return memo[n];
  }
  return fibonacci(n);
};

// Time complexity is O(2^n) since we are making two recursive calls in the same function

// Space complexity is O(n) for the recursion stack

console.log(calcFibonacci(100));
