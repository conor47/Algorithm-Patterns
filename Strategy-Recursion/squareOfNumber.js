// Implement a function that takes a number testVariable and returns the square of the number. Try using the following mathematical identity to solve this problem.  (n−1)2=n2−2n+1

function square(num) {
  if (num === 0) {
    return 0;
  } else {
    return square(num - 1) + 2 * num - 1;
  }
}

console.log(square(5));
