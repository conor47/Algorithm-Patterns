// Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

// Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.

// Example 1:

// Input: [3, 1, 5, 12, 2, 11], K = 3
// Output: [5, 12, 11]

// Example 2:

// Input: [5, 12, 11, -1, 12], K = 3
// Output: [12, 11, 12]

const heap = require('collections/heap');

function k_largest_numbers(nums, k) {
  const minHeap = new heap([], null, (a, b) => b - a);

  //   put first k elements into heap
  for (i = 0; i < k; i++) {
    minHeap.push(nums[i]);
  }

  //   iterate through remaining elements

  for (i = k; i < nums.length; i++) {
    if (nums[i] > minHeap.peek()) {
      minHeap.pop();
      minHeap.push(nums[i]);
    }
  }

  return minHeap.toArray();
}

// time complexity is O(k * log K * (n - k)*logk) which is asymptotically equivalent to O(n * logk)

// space complexity is O(k) since we are storing top k elements in the heap

console.log(
  `Here are the top K numbers: ${find_k_largest_numbers(
    [3, 1, 5, 12, 2, 11],
    3
  )}`
);
console.log(
  `Here are the top K numbers: ${find_k_largest_numbers(
    [5, 12, 11, -1, 12],
    3
  )}`
);
