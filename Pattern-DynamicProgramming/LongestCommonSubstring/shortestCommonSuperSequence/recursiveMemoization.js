// Given two sequences ‘s1’ and ‘s2’, write a method to find the length of the shortest sequence which has ‘s1’ and ‘s2’ as subsequences.

// Example 2:

// Input: s1: "abcf" s2:"bdcf"
// Output: 5
// Explanation: The shortest common super-sequence (SCS) is "abdcf".

// Example 2:

// Input: s1: "dynamic" s2:"programming"
// Output: 15
// Explanation: The SCS is "dynprogrammicng".

const findSCSLength = function (s1, s2) {
  const dp = [];
  function recursive(s1, s2, idx1, idx2) {
    if (idx1 === s1.length) return s2.length - idx2;
    if (idx2 === s2.length) return s1.length - idx1;

    let key = `${idx1}-${idx2}`;
    if (typeof dp[key] === 'undefined') {
      if (s1[idx1] === s2[idx2]) {
        return 1 + recursive(s1, s2, idx1 + 1, idx2 + 1);
      }

      let c1 = 1 + recursive(s1, s2, idx1 + 1, idx2);
      let c2 = 1 + recursive(s1, s2, idx1, idx2 + 1);

      dp[key] = Math.min(c1, c2);
    }
    return dp[key];
  }
  return recursive(s1, s2, 0, 0);
};

console.log(
  `Length of Shortest Common Subsequence: Substring: ---> ${findSCSLength(
    'abcf',
    'bdcf'
  )}`
);
console.log(
  `Length of Shortest Common Subsequence: Substring: ---> ${findSCSLength(
    'dynamic',
    'programming'
  )}`
);
