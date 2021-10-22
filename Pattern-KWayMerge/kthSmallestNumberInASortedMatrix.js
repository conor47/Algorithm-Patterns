// Given an N∗NN * NN∗N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.

// Example 1:

// Input: Matrix=[
//     [2, 6, 8],
//     [3, 7, 10],
//     [5, 8, 11]
//   ],
//   K=5
// Output: 7
// Explanation: The 5th smallest number in the matrix is 7.

const heap = require('collections/heap');

const find_Kth_smallest = function (matrix, k) {
  let minHeap = new heap([], null, (a, b) => b[0] - a[0]);

  for (let i = 0; i < matrix.length; i++) {
    minHeap.push([matrix[i][0], 0, matrix[i]]);
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

// Time complexity is O()

// Space complexity is O(N) as in the worst case we store one number from each row in the heap

console.log(
  `Kth smallest number is: ${find_Kth_smallest(
    [
      [2, 6, 8],
      [3, 7, 10],
      [5, 8, 11],
    ],
    5
  )}`
);
