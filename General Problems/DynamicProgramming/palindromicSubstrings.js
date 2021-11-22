// Given a string s, return the number of palindromic substrings in it.

// A string is a palindrome when it reads the same backward as forward.

// A substring is a contiguous sequence of characters within the string.

// Example 1:

// Input: s = "abc"
// Output: 3
// Explanation: Three palindromic strings: "a", "b", "c".

// Example 2:

// Input: s = "aaa"
// Output: 6
// Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

// Constraints:

//     1 <= s.length <= 1000
//     s consists of lowercase English letters.

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
