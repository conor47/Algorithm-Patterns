// Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

// Example 1:

// Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
// Output: 4
// Explanation: The 5th smallest number among all the arrays is 4, this can be verified from
// the merged list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]

// Example 2:

// Input: L1=[5, 8, 9], L2=[1, 7], K=3
// Output: 7
// Explanation: The 3rd smallest number among all the arrays is 7.

const heap = require('collections/heap');

const find_Kth_smallest = function (lists, k) {
  let minHeap = new heap([], null, (a, b) => b[0] - a[0]);

  //   push the first value of each list into the heap
  for (let i = 0; i < lists.length; i++) {
    minHeap.push([lists[i][0], 0, lists[i]]);
  }

  let numberCount = 0;
  let number = 0;
  while (minHeap.length > 0) {
    [number, i, list] = minHeap.pop();
    numberCount += 1;
    if (numberCount === k) {
      break;
    }
    if (list[i + 1]) {
      minHeap.push([list[i + 1], i + 1, list]);
    }
  }

  return number;
};

// Time complexity is O(K * Log M) where M is the number of input arrays

// Space complexity

console.log(
  `Kth smallest number is: ${find_Kth_smallest(
    [
      [2, 6, 8],
      [3, 6, 7],
      [1, 3, 4],
    ],
    5
  )}`
);
