function factorial(targetNumber) {
  // Base case
  if (targetNumber <= 1) {
    // Factorial of 1 is 1
    return 1;
  }

  // Recursive case
  else {
    return targetNumber * factorial(targetNumber - 1); // Factorial of any other number is
    // number multiplied by factorial of number - 1
  }
}
// Driver Code
var targetNumber = 5;
var result = factorial(targetNumber);
console.log('The factorial of ' + targetNumber + ' is: ' + result);
