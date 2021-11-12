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
      }
    }
  }
};
