// Given a string, find the total number of palindromic substrings in it. Please note we need to find the total number of substrings and not subsequences.

// Example 1:

// Input: "abdbca"
// Output: 7
// Explanation: Here are the palindromic substrings, "a", "b", "d", "b", "c", "a", "bdb".

// Example 2:

// Input: = "cddpd"
// Output: 7
// Explanation: Here are the palindromic substrings, "c", "d", "d", "p", "d", "dd", "dpd".

// Example 3:

// Input: = "pqr"
// Output: 3
// Explanation: Here are the palindromic substrings,"p", "q", "r".

var countSubstrings = function (str) {
  const dp = [];
  count = 0;
  for (let i = 0; i < str.length; i++) {
    for (let j = i; j < str.length; j++) {
      count += helper(str, i, j, dp);
    }
  }
  return count;
};

const helper = function (str, i, j, dp) {
  if (i >= j) {
    return 1;
  }
  key = `${i}-${j}`;
  if (typeof dp[key] === 'undefined') {
    dp[key] = str[i] === str[j] ? helper(str, i + 1, j - 1, dp) : 0;
  }
  return dp[key];
};
