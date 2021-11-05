// Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. The range of the ‘key’ will be the first and last position of the ‘key’ in the array.

// Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

// Example 1:

// Input: [4, 6, 6, 6, 9], key = 6
// Output: [1, 3]

// Example 2:

// Input: [1, 3, 8, 10, 15], key = 10
// Output: [3, 3]

// Example 3:

// Input: [1, 3, 8, 10, 15], key = 12
// Output: [-1, -1]

const find_range = function (arr, key) {
  result = [-1, -1];
  result[0] = binary_search(arr, key, false);
  if (result[0] !== -1) {
    result[1] = binary_search(arr, key, true);
  }
  return result;
};

const binary_search = function (arr, key, findMax) {
  let keyIndex = -1;
  let start = 0;
  let end = arr.length - 1;
  while (start <= end) {
    let mid = Math.floor(start + (end - start) / 2);
    if (arr[mid] < key) start = mid + 1;
    else if (arr[mid] > key) end = mid - 1;
    else {
      keyIndex = mid;
      //   if the findMax flag is set then we want to try to find the max index of the key
      if (findMax) {
        start = mid + 1;
        // if the findMax flag is not set then we want to find the smallest index of the key
      } else {
        end = mid - 1;
      }
    }
  }
  return keyIndex;
};

// Time complexity is O(log N)

// Space complexity is O(1)

console.log(find_range([4, 6, 6, 6, 9], 6));
console.log(find_range([1, 3, 8, 10, 15], 10));
console.log(find_range([1, 3, 8, 10, 15], 12));
