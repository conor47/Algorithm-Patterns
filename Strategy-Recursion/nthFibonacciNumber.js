// Implement a function that takes a variable testVariable and finds the number that is placed at that index in the Fibonacci sequence.

function fibonacci(testVariable) {
  if (testVariable <= 1) return testVariable;

  return fibonacci(testVariable - 1) + fibonacci(testVariable - 2);
}

console.log(fibonacci(10));
