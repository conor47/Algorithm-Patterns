// Given strings s1 and s2, we need to transform s1 into s2 by deleting and inserting characters. Write a function to calculate the count of the minimum number of deletion and insertion operations.

// Example 1:

// Input: s1 = "abc"
//        s2 = "fbc"
// Output: 1 deletion and 1 insertion.
// Explanation: We need to delete {'a'} and insert {'f'} to s1 to transform it into s2.

// Example 2:

// Input: s1 = "abdca"
//        s2 = "cbda"
// Output: 2 deletions and 1 insertion.
// Explanation: We need to delete {'a', 'c'} and insert {'c'} to s1 to transform it into s2.

// Example 3:

// Input: s1 = "passport"
//        s2 = "ppsspt"
// Output: 3 deletions and 1 insertion
// Explanation: We need to delete {'a', 'o', 'r'} and insert {'p'} to s1 to transform it into s2.

const findMDI = function (s1, s2) {
  const dp = [];
  const recursive = function (s1, s2, index1, index2) {
    if (index1 === s1.length || index2 === s2.length) {
      return 0;
    }

    dp[index1] = dp[index1] || [];

    if (typeof dp[index1][index2] === 'undefined') {
      if (s1[index1] === s2[index2]) {
        return 1 + recursive(s1, s2, index1 + 1, index2 + 1);
      }
      let c1 = recursive(s1, s2, index1, index2 + 1);
      let c2 = recursive(s1, s2, index1 + 1, index2);

      dp[index1][index2] = Math.max(c1, c2);
    }
    return dp[index1][index2];
  };
  let common = recursive(s1, s2, 0, 0);
  let deletions = s1.length - common;
  let insertions = s2.length - common;
  return insertions + deletions;
};

// Time complexity is O(M * N) where M and N are the lenghts of the input strings

// Space complexity is O(M * N)

console.log(findMDI('abc', 'fbc'));
console.log(findMDI('abdca', 'cbda'));
console.log(findMDI('passport', 'ppsspt'));
