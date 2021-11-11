// Write a function to calculate the nth Fibonacci number.

const fibonacci = function (n) {
  if (n < 2) {
    return n;
  }

  return fibonacci(n - 1) + fibonacci(n - 2);
};

// Time complexity is O(2^n) since we are making two recursive calls in the same function

// Space complexity is O(n) for the recursion stack
