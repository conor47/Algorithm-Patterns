// Given two strings ‘s1’ and ‘s2’, find the length of the longest subsequence which is common in both the strings.

// A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

// Example 1:

// Input: s1 = "abdca"
//        s2 = "cbda"
// Output: 3
// Explanation: The longest common subsequence is "bda".

// Example 2:

// Input: s1 = "passport"
//        s2 = "ppsspt"
// Output: 5
// Explanation: The longest common subsequence is "psspt".

const findLCSLength = function (s1, s2) {
  const dp = [];
  const recursive = function (s1, s2, idx1, idx2) {
    if (idx1 === s1.length || idx2 === s2.length) {
      return 0;
    }

    dp[idx1] = dp[idx1] || [];

    if (typeof dp[idx1][idx2] === 'undefined') {
      if (s1[idx1] === s2[idx2]) {
        dp[idx1][idx2] = 1 + recursive(s1, s2, idx1 + 1, idx2 + 1);
      } else {
        let c1 = recursive(s1, s2, idx1 + 1, idx2);
        let c2 = recursive(s1, s2, idx1, idx2 + 1);
        dp[idx1][idx2] = Math.max(c1, c2);
      }
    }
    return dp[idx1][idx2];
  };
  return recursive(s1, s2, 0, 0);
};

console.log(
  `Length of Longest Common Subsequence: ---> ${findLCSLength('abdca', 'cbda')}`
);
console.log(
  `Length of Longest Common Subsequence: ---> ${findLCSLength(
    'passport',
    'ppsspt'
  )}`
);
