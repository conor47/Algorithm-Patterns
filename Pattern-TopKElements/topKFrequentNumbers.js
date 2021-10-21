// Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

// Example 1:

// Input: [1, 3, 5, 12, 11, 12, 11], K = 2
// Output: [12, 11]
// Explanation: Both '11' and '12' apeared twice.

// Example 2:

// Input: [5, 12, 11, 3, 11], K = 2
// Output: [11, 5] or [11, 12] or [11, 3]
// Explanation: Only '11' appeared twice, all other numbers appeared once.

const heap = require('collections/heap');

const find_k_frequent_numbers = function (nums, k) {
  let frequencyCount = {};
  for (let num of nums) {
    if (!(num in frequencyCount)) frequencyCount[num] = 1;
    else frequencyCount[num] += 1;
  }

  let minHeap = new heap([], null, (a, b) => b[0] - a[0]);
  Object.keys(frequencyCount).forEach((num) => {
    minHeap.push([frequencyCount[num], num]);
    if (minHeap.length > k) {
      minHeap.pop();
    }
  });
  let topNumbers = [];
  while (minHeap.length > 0) {
    topNumbers.push(minHeap.pop()[1]);
  }
  return topNumbers;
};

// Time complexity is O(n * log k)

// Space complexity is O(n) since we need to store all of the elements and their counts in the hashmap

console.log(
  `Here are the K frequent numbers: ${find_k_frequent_numbers(
    [1, 3, 5, 12, 11, 12, 11],
    2
  )}`
);
console.log(
  `Here are the K frequent numbers: ${find_k_frequent_numbers(
    [5, 12, 11, 3, 11],
    2
  )}`
);
