// Given two strings ‘s1’ and ‘s2’, find the length of the longest substring which is common in both the strings.

// Example 1:

// Input: s1 = "abdca"
//        s2 = "cbda"
// Output: 2
// Explanation: The longest common substring is "bd".

// Example 2:

// Input: s1 = "passport"
//        s2 = "ppsspt"
// Output: 3
// Explanation: The longest common substring is "ssp".

const findLCSLength = function (s1, s2) {
  const recursive = function (s1, s2, idx1, idx2, count) {
    if (idx1 === s1.length || idx2 === s2.length) {
      return count;
    }

    if (s1[idx1] === s2[idx2]) {
      count = recursive(s1, s2, idx1 + 1, idx2 + 1, count + 1);
    }

    let c1 = recursive(s1, s2, idx1 + 1, idx2, 0);
    let c2 = recursive(s1, s2, idx1, idx2 + 1, 0);

    return Math.max(count, Math.max(c1, c2));
  };
  return recursive(s1, s2, 0, 0, 0);
};

console.log(
  `Length of Longest Common Substring: ---> ${findLCSLength('abdca', 'cbda')}`
);
console.log(
  `Length of Longest Common Substring: ---> ${findLCSLength(
    'passport',
    'ppsspt'
  )}`
);
