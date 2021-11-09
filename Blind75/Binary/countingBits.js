// Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

// Example 1:

// Input: n = 2
// Output: [0,1,1]
// Explanation:
// 0 --> 0
// 1 --> 1
// 2 --> 10

// Example 2:

// Input: n = 5
// Output: [0,1,1,2,1,2]
// Explanation:
// 0 --> 0
// 1 --> 1
// 2 --> 10
// 3 --> 11
// 4 --> 100
// 5 --> 101

// Constraints:

//     0 <= n <= 105

var countBits = function (n) {
  let result = Array(n + 1);
  for (let i = 0; i <= n; i++) {
    let ones = onesCount(i);
    result[i] = ones;
  }
  return result;
};

let onesCount = function (n) {
  let mask = 1;
  let bits = 0;
  for (let i = 0; i < 32; i++) {
    if ((n & mask) !== 0) {
      bits += 1;
    }
    mask = mask << 1;
  }
  return bits;
};

// Space complexity is O(1)
