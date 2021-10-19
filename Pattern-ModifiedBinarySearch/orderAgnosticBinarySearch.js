// Given a sorted array of numbers, find if a given number ‘key’ is present in the array. Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. You should assume that the array can have duplicates.

// Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

// Example 1:

// Input: [4, 6, 10], key = 10
// Output: 2

// Example 2:

// Input: [1, 2, 3, 4, 5, 6, 7], key = 5
// Output: 4

// Example 3:

// Input: [10, 6, 4], key = 10
// Output: 0

// Example 4:

// Input: [10, 6, 4], key = 4
// Output: 2

const binary_search = function (arr, key) {
  let start = 0;
  let end = arr.length - 1;
  let isAscending = arr[start] < arr[end];
  while (start < end) {
    let mid = Maths.abs(Math.floor(start - (end - start) / 2));

    if (arr[mid] === key) {
      return mid;
    }
    if (isAscending) {
      if (key < arr[mid]) {
        end = mid - 1;
      } else {
        start = mid + 1;
      }
    } else {
      if (key < arr[mid]) {
        start = mid + 1;
      } else {
        end = mid - 1;
      }
    }
  }
  return -1;
};

// Time complexity is still O(Log N) where N is the number of elements in the input array

// Space complexity is O(1)

console.log(binary_search([4, 6, 10], 10));
console.log(binary_search([1, 2, 3, 4, 5, 6, 7], 5));
console.log(binary_search([10, 6, 4], 10));
console.log(binary_search([10, 6, 4], 4));
