// Given a string s. In one step you can insert any character at any index of the string.

// Return the minimum number of steps to make s palindrome.

// A Palindrome String is one that reads the same backward as well as forward.

// Example 1:

// Input: s = "zzazz"
// Output: 0
// Explanation: The string "zzazz" is already palindrome we don't need any insertions.

// Example 2:

// Input: s = "mbadm"
// Output: 2
// Explanation: String can be "mbdadbm" or "mdbabdm".

// Example 3:

// Input: s = "leetcode"
// Output: 5
// Explanation: Inserting 5 characters the string becomes "leetcodocteel".

// Example 4:

// Input: s = "g"
// Output: 0

// Example 5:

// Input: s = "no"
// Output: 1

// Constraints:

//     1 <= s.length <= 500
//     All characters of s are lower case English letters.

const minInsertions = function (str) {
  const dp = [];
  let lps = recursive(str, 0, str.length - 1, dp);
  if (lps === str.length) {
    return 0;
  }
  if (lps < str.length) {
    return str.length - lps;
  }
};

const recursive = function (str, start, end, dp) {
  if (start > end) {
    return 0;
  }

  if (start === end) {
    return 1;
  }

  let key = `${start}-${end}`;

  if (typeof dp[key] === 'undefined') {
    if (str[start] === str[end]) {
      return 2 + recursive(str, start + 1, end - 1, dp);
    }

    let c1 = recursive(str, start + 1, end, dp);
    let c2 = recursive(str, start, end - 1, dp);

    dp[key] = Math.max(c1, c2);
  }
  return dp[key];
};

// Time complexity is O(n^2)
// Space complexity is O(n^2)
