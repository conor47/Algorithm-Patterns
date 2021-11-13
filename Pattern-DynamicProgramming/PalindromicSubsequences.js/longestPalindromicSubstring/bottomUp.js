const findLPS = function (str) {
  let max = 1;
  const dp = Array(str.length)
    .fill(0)
    .map(() => Array(str.length).fill(0));

  for (let i = 0; i < str.length; i++) {
    dp[i][i] = true;
  }

  for (let start = str.length - 1; start >= 0; start--) {
    for (let end = start + 1; end < str.length; end++) {
      if (str[start] === str[end]) {
        if (end - start === 1 || dp[start + 1][end - 1]) {
          dp[start][end] = true;
          max = Math.max(max, end - start + 1);
        }
      }
    }
  }

  return max;
};

console.log(`Length of LPS ---> ${findLPS('abdbca')}`);
console.log(`Length of LPS ---> ${findLPS('cddpd')}`);
console.log(`Length of LPS ---> ${findLPS('pqr')}`);
