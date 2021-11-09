// Given two integers a and b, return the sum of the two integers without using the operators + and -.

// Example 1:

// Input: a = 1, b = 2
// Output: 3

// Example 2:

// Input: a = 2, b = 3
// Output: 5

let getSum = function (a, b) {
  let carry;

  while ((a & b) !== 0) {
    carry = (a & b) << 1;
    a = a ^ b;
    b = carry;
  }

  return a ^ b;
};

// Time complexity is O(1)

// space complexity is O(1)
