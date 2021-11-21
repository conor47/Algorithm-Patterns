// Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

// A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

// Example 1:

// Input: str1 = "abac", str2 = "cab"
// Output: "cabac"
// Explanation:
// str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
// str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
// The answer provided is the shortest such string that satisfies these properties.

// Example 2:

// Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
// Output: "aaaaaaaa"

// Constraints:

//     1 <= str1.length, str2.length <= 1000
//     str1 and str2 consist of lowercase English letters.

var shortestCommonSupersequence = function (s1, s2) {
  const dp = Array(s1.length + 1)
    .fill()
    .map(() => Array(s2.length + 1).fill());

  for (let i = 0; i <= s1.length; i++) {
    dp[i][0] = s1.substring(0, i);
  }

  for (let j = 0; j <= s2.length; j++) {
    dp[0][j] = s2.substring(0, j);
  }

  for (let i = 1; i <= s1.length; i++) {
    for (let j = 1; j <= s2.length; j++) {
      if (s1[i - 1] === s2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + s1[i - 1];
      } else {
        if (dp[i - 1][j].length < dp[i][j - 1].length) {
          dp[i][j] = dp[i - 1][j] + s1[i - 1];
        } else {
          dp[i][j] = dp[i][j - 1] + s2[j - 1];
        }
      }
    }
  }

  return dp[s1.length][s2.length];
};

// Time complexity is O(L1L2) where L1 and L2 are the lengths of the input strings

// Space complexity is O(L1L2)
