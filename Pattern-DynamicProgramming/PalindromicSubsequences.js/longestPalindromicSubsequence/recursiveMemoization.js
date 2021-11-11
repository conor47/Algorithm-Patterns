// Given a sequence, find the length of its Longest Palindromic Subsequence (LPS). In a palindromic subsequence, elements read the same backward and forward.

// A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

// Example 1:

// Input: "abdbca"
// Output: 5
// Explanation: LPS is "abdba".

// Example 2:

// Input: = "cddpd"
// Output: 3
// Explanation: LPS is "ddd".

// Example 3:

// Input: = "pqr"
// Output: 1
// Explanation: LPS could be "p", "q" or "r".

const findLPSLength = function (st) {
  dp = [];
  function recursive(st, start, end) {
    if (start > end) {
      return 0;
    }

    if (start === end) {
      return 1;
    }

    dp[start] = dp[start] || [];

    if (typeof dp[start][end] === 'undefined') {
      if (st[start] === st[end]) {
        dp[start][end] = 2 + recursive(st, start + 1, end - 1);
      } else {
        let a = recursive(st, start + 1, end);
        let b = recursive(st, start, end - 1);
        dp[start][end] = Math.max(a, b);
      }
    }
    return dp[start][end];
  }
  return recursive(st, 0, st.length - 1);
};

// Time complexity is O(N^2) since this is the size of our memoization array

// Space complexity is O(N^2) for the memoization array. The recursion stack uses O(N)

console.log('Length of LPS ---> ' + findLPSLength('abdbca'));
console.log('Length of LPS ---> ' + findLPSLength('cddpd'));
console.log('Length of LPS ---> ' + findLPSLength('pqr'));
