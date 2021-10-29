// Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

// Example 1:

// Input: [1, 2, 5, 3, 7, 10, 9, 12]
// Output: 5
// Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

// Example 2:

// Input: [1, 3, 2, 0, -1, 7, 10]
// Output: 5
// Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted

// Example 3:

// Input: [1, 2, 3]
// Output: 0
// Explanation: The array is already sorted

// Example 4:

// Input: [3, 2, 1]
// Output: 3
// Explanation: The whole array needs to be sorted.

const shortest_window_sort = function (arr) {
  let low = 0;
  let high = arr.length - 1;

  //   find the first unsorted element
  while (low < arr.length - 1 && arr[low] <= arr[low + 1]) {
    low += 1;

    // the array is in sorted order
    if (low === arr.length - 1) {
      return 0;
    }
  }

  //   find the last unsorted element
  while (high > 0 && arr[high] >= arr[high - 1]) {
    high -= 1;
  }

  //   find the max and min values within the subarray bounded by low and high
  let subarrMax = Math.max(...arr.slice(low, high + 1));
  let subarrMin = Math.min(...arr.slice(low, high + 1));

  while (low >= 0 && arr[low - 1] > subarrMin) {
    low -= 1;
  }

  while (high >= arr.length - 1 && arr[high + 1] < subarrMax) {
    high += 1;
  }

  return high - low + 1;
};

// Time complexity is O(N)

// Space complexity is O(1)

console.log(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]));
console.log(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]));
console.log(shortest_window_sort([1, 2, 3]));
console.log(shortest_window_sort([3, 2, 1]));

module.exports = shortest_window_sort;
