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
  const recursive = function (s1, s2, idx1, idx2) {
    if (idx1 === s1.length || idx2 === s2.length) {
      return 0;
    }

    if (s1[idx1] === s2[idx2]) {
      return 1 + recursive(s1, s2, idx1 + 1, idx2 + 1);
    }

    let c1 = recursive(s1, s2, idx1 + 1, idx2);
    let c2 = recursive(s1, s2, idx1, idx2 + 1);

    return Math.max(c1, c2);
  };
  return recursive(s1, s2, 0, 0);
};

// Time complexity is O(2^(M+N)) where M and N are the lengths of the two input strings

// Space complexity is O(M +N)

console.log(
  `Length of Longest Common Subsequence: ---> ${findLCSLength('abdca', 'cbda')}`
);
console.log(
  `Length of Longest Common Subsequence: ---> ${findLCSLength(
    'passport',
    'ppsspt'
  )}`
);
