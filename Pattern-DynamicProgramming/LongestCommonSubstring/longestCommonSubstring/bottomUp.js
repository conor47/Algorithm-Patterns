const findLCSLength = function (s1, s2) {
  const dp = Array(s1.length + 1)
    .fill(0)
    .map(() => Array(s2.length + 1).fill(0));

  let maxLength = 0;

  for (let i = 1; i <= s1.length; i++) {
    for (let j = 1; j <= s2.length; j++) {
      if (s1[i - 1] === s2[j - 1]) {
        dp[i][j] = 1 + dp[i - 1][j - 1];
        maxLength = Math.max(dp[i][j], maxLength);
      }
    }
  }
  return maxLength;
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

// Time complexity is O(N * M) where N and M are the lenghts of the input strings

// Space complexity is O(M * N)
