const findLPSLength = function (st) {
  let dp = Array(st.length)
    .fill(0)
    .map(() => Array(st.length).fill(0));

  for (let i = 0; i < st.length; i++) {
    dp[i][i] = 1;
  }

  for (let startIndex = st.length - 1; startIndex >= 0; startIndex--) {
    for (let endIndex = startIndex + 1; endIndex < st.length; endIndex++) {
      if (st[endIndex] === st[startIndex]) {
        dp[startIndex][endIndex] = 2 + dp[startIndex + 1][endIndex - 1];
      } else {
        dp[startIndex][endIndex] = Math.max(
          dp[startIndex][endIndex - 1],
          dp[startIndex + 1][endIndex - 1]
        );
      }
    }
  }

  return dp[0][dp.length - 1];
};

// Time complexity is O(n^2)

// Space complexity is O(n^2)

console.log('Length of LPS ---> ' + findLPSLength('abdbca'));
console.log('Length of LPS ---> ' + findLPSLength('cddpd'));
console.log('Length of LPS ---> ' + findLPSLength('pqr'));
