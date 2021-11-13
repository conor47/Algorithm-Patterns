// Given a string, find the length of its Longest Palindromic Substring (LPS). In a palindromic string, elements read the same backward and forward.

// Example 1:

// Input: "abdbca"
// Output: 3
// Explanation: LPS is "bdb".

// Example 2:

// Input: = "cddpd"
// Output: 3
// Explanation: LPS is "dpd".

// Example 3:

// Input: = "pqr"
// Output: 1
// Explanation: LPS could be "p", "q" or "r".

const longestSub = function (str) {
  const dp = [];
  const recursive = function (str, start, end) {
    if (start > end) {
      return 0;
    }

    if (start === end) {
      return 1;
    }

    dp[start] = dp[start] || [];

    if (typeof dp[start][end] === 'undefined') {
      if (str[start] === str[end]) {
        const remainingLength = end - start - 1;
        if (remainingLength === recursive(str, start + 1, end - 1)) {
          return 2 + remainingLength;
        }
      }

      let c1 = recursive(str, start + 1, end);
      let c2 = recursive(str, start, end - 1);

      dp[start][end] = Math.max(c1, c2);
    }

    return dp[start][end];
  };

  return recursive(str, 0, str.length - 1);
};

// Time complexity is O(N^2) as we will have no more than N * N subproblems

// Space complexity is O(N^2) due to the memoization matrix

console.log(`Length of LPS ---> ${longestSub('abdbca')}`);
console.log(`Length of LPS ---> ${longestSub('cddpd')}`);
console.log(`Length of LPS ---> ${longestSub('pqr')}`);
