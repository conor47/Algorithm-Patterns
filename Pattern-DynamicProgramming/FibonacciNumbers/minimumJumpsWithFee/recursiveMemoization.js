const findMinFee = function (fee) {
  const dp = [];
  function countMin(fee, currentIndex) {
    if (typeof dp[currentIndex] === 'undefined') {
      if (currentIndex > fee.length - 1) return 0;

      let total1 = countMin(fee, currentIndex + 1);
      let total2 = countMin(fee, currentIndex + 2);
      let total3 = countMin(fee, currentIndex + 3);
      let min = Math.min(total1, total2, total3);

      dp[currentIndex] = min + fee[currentIndex];
    }
    return dp[currentIndex];
  }
  return countMin(fee, 0);
};

console.log(`Minimum fee needed: ---> ${findMinFee([1, 2, 5, 2, 1, 2])}`);
console.log(`Minimum fee needed: ---> ${findMinFee([2, 3, 4, 5])}`);
