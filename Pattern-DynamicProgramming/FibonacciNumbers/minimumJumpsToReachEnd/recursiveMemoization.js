// Given an array of positive numbers, where each element represents the max number of jumps that can be made forward from that element, write a program to find the minimum number of jumps needed to reach the end of the array (starting from the first element). If an element is 0, then we cannot move through that element.

// Example 1:

// Input = {2,1,1,1,4}
// Output = 3
// Explanation: Starting from index '0', we can reach the last index through: 0->2->3->4

// Example 2:

// Input = {1,1,3,6,9,3,0,1,3}
// Output = 4
// Explanation: Starting from index '0', we can reach the last index through: 0->1->2->3->8

const countMinJumps = function (jumps) {
  const dp = [];
  function countMin(jumps, CurrentIndex) {
    if (CurrentIndex === jumps.length - 1) return 0;

    if (jumps[CurrentIndex] === 0) return Number.MAX_VALUE;

    if (typeof dp[CurrentIndex] === 'undefined') {
      let totalJumps = Number.MAX_VALUE;
      let start = CurrentIndex + 1;
      let end = CurrentIndex + jumps[CurrentIndex];
      while (start < jumps.length && start <= end) {
        const minJumps = countMin(jumps, start++);
        if (minJumps !== Number.MAX_VALUE) {
          totalJumps = Math.min(totalJumps, minJumps + 1);
        }
        dp[CurrentIndex] = totalJumps;
      }
    }

    return dp[CurrentIndex];
  }
  return countMin(jumps, 0);
};

console.log(`Minimum jumps needed: ---> ${countMinJumps([2, 1, 1, 1, 4])}`);
console.log(
  `Minimum jumps needed: ---> ${countMinJumps([1, 1, 3, 6, 9, 3, 0, 1, 3])}`
);
