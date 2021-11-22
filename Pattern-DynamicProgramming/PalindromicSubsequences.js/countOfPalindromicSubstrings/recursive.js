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

var findCPS = function (str) {
  count = 0;
  for (let i = 0; i < str.length; i++) {
    for (let j = i; j < str.length; j++) {
      count += helper(str, i, j);
    }
  }
  return count;
};

const helper = function (str, i, j) {
  if (i >= j) {
    return 1;
  }

  return str[i] === str[j] ? helper(str, i + 1, j - 1) : 0;
};

console.log('Length of LPS: ---> ' + findCPS('abdbca'));
console.log('Length of LPS: ---> ' + findCPS('cddpd'));
console.log('Length of LPS: ---> ' + findCPS('pqr'));
