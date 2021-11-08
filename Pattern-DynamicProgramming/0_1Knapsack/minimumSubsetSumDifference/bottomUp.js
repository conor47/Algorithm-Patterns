const canPartition = function (num) {
  let n = num.length;
  let sum = 0;
  //   calculate the sum of the numbers in num array
  for (let i = 0; i < n; i++) {
    sum += num[i];
  }

  let requiredSum = Math.floor(sum / 2);

  //   build out grid
  let dp = Array(n)
    .fill(false)
    .map(() => Array(requiredSum + 1).fill(false));

  //   fill first column with true
  for (let i = 0; i < n; i++) {
    dp[i][0] = true;
  }

  // fill first row
  for (let i = 1; i <= requiredSum; i++) {
    dp[0][i] = i === num[0];
  }

  // fill grid / process all subsets

  for (let i = 1; i < n; i++) {
    for (let j = 1; j <= requiredSum; j++) {
      if (dp[i - 1][j]) {
        dp[i][j] = dp[i - 1][j];
      } else {
        dp[i][j] = dp[i - 1][j - num[i]];
      }
    }
  }

  let sum1 = 0;

  for (let i = requiredSum; i >= 0; i--) {
    if (dp[n - 1][i] === true) {
      sum1 = i;
      break;
    }
  }

  let sum2 = sum - sum1;
  return Math.abs(sum2 - sum1);
};

console.log(`Minimum subset difference is: ---> ${canPartition([1, 2, 3, 9])}`);
console.log(
  `Minimum subset difference is: ---> ${canPartition([1, 2, 7, 1, 5])}`
);
console.log(
  `Minimum subset difference is: ---> ${canPartition([1, 3, 100, 4])}`
);
