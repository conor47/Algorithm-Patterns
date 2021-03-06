const findMDI = function (s1, s2) {
  const lcs = recursive(s1, s2);
  let deletions = s1.length - lcs;
  let additions = s2.length - lcs;
  return additions + deletions;
};

const recursive = function (s1, s2) {
  const dp = Array(s1.length + 1)
    .fill(0)
    .map(() => Array(s2.length + 1).fill(0));

  for (let i = 1; i <= s1.length; i++) {
    for (let j = 1; j <= s2.length; j++) {
      if (s1[i - 1] === s2[j - 1]) {
        dp[i][j] = 1 + dp[i - 1][j - 1];
      } else {
        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }
  return dp[s1.length][s1.length];
};

// time complexity is O(M * N)

// space complexity is O(M * N)

console.log(findMDI('abc', 'fbc'));
console.log(findMDI('abdca', 'cbda'));
console.log(findMDI('passport', 'ppsspt'));
