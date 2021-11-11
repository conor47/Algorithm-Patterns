// We are given a ribbon of length ‘n’ and a set of possible ribbon lengths. We need to cut the ribbon into the maximum number of pieces that comply with the above-mentioned possible lengths. Write a method that will return the count of pieces.

// Example 1:

// n: 5
// Ribbon Lengths: {2,3,5}
// Output: 2
// Explanation: Ribbon pieces will be {2,3}.

// Example 2:

// n: 7
// Ribbon Lengths: {2,3}
// Output: 3
// Explanation: Ribbon pieces will be {2,2,3}.

// Example 3:

// n: 13
// Ribbon Lengths: {3,5,7}
// Output: 3
// Explanation: Ribbon pieces will be {3,3,7}.

let countRibbonPieces = function (ribbonLengths, total) {
  let ans;
  let recursive = function (lengths, total, index) {
    if (total === 0) {
      return 0;
    }

    if (total < 0 || index >= lengths.length) {
      return Number.MIN_VALUE;
    }

    let total1 = Number.MIN_VALUE;
    if (lengths[index] <= total) {
      let res = recursive(lengths, total - lengths[index], index);
      if (res !== Number.MIN_VALUE) {
        total1 = res + 1;
      }
    }

    let total2 = recursive(lengths, total, index + 1);

    return Math.max(total1, total2);
  };

  ans = recursive(ribbonLengths, total, 0);
  return ans === Number.MIN_VALUE ? -1 : ans;
};

console.log(
  `Maximum number of ribbons: ---> ${countRibbonPieces([2, 3, 5], 5)}`
);
console.log(`Maximum number of ribbons: ---> ${countRibbonPieces([2, 3], 7)}`);
console.log(
  `Maximum number of ribbons: ---> ${countRibbonPieces([3, 5, 7], 13)}`
);
console.log(`Maximum number of ribbons: ---> ${countRibbonPieces([3, 5], 7)}`);
