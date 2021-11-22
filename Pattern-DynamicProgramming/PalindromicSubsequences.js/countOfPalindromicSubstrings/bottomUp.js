const findCPS = function (str) {
  const dp = Array(str.length)
    .fill(false)
    .map(() => Array(str.length).fill(false));

  let count = 0;

  for (let i = 0; i < str.length; i++) {
    dp[i][i] = true;
    count++;
  }

  for (let start = str.length - 1; start >= 0; start--) {
    for (let end = start + 1; end < str.length; end++) {
      if (str[start] === str[end]) {
        if (end - start == 1 || dp[start + 1][end - 1]) {
          dp[start][end] = true;
          count++;
        }
      }
    }
  }

  return count;
};

// Time complexity is O(N^2) where N is the length of the input string

// Space complexity is O(N^2)

console.log('Length of LPS: ---> ' + findCPS('abdbca'));
console.log('Length of LPS: ---> ' + findCPS('cddpd'));
console.log('Length of LPS: ---> ' + findCPS('pqr'));
