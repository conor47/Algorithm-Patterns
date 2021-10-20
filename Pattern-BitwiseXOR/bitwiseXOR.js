// Given an array of n−1 integers in the range from 1 to n, find the one number that is missing from the array.

// Example:

// Input: 1, 5, 2, 6, 4
// Answer: 3

function find_missing_number(arr) {
  let n = arr.length + 1;

  let x1 = 1;
  for (let i = 2; i <= n; i++) {
    x1 = x1 ^ i;
  }

  let x2 = arr[0];
  for (let i = 1; i < n - 1; i++) {
    x2 = x2 ^ arr[i];
  }

  return x1 ^ x2;
}

console.log(`Missing number is: ${find_missing_number([1, 5, 2, 6, 4])}`);
