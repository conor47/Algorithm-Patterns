// Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

// Example 1:

// Input: [1, 3, 8, 12, 4, 2]
// Output: 12
// Explanation: The maximum number in the input bitonic array is '12'.

// Example 2:

// Input: [3, 8, 3, 1]
// Output: 8

// Example 3:

// Input: [1, 3, 8, 12]
// Output: 12

// Example 4:

// Input: [10, 9, 8]
// Output: 10

const find_max_in_bitonic_array = function (arr) {
  let start = 0;
  let end = arr.length - 1;
  if (arr[0] > arr[1]) return arr[0];
  if (arr[end] > arr[end - 1]) return arr[end];
  while (start <= end) {
    let mid = Math.floor(start + (end - start) / 2);
    if (arr[mid] > arr[mid - 1] && arr[mid] > arr[mid + 1]) return arr[mid];
    else if (arr[mid] < arr[mid - 1]) end = mid - 1;
    else start = mid + 1;
  }
  return -1;
};

// alternative solution. Same approach, less code

const find_max_bitonic_array_v2 = function (arr) {
  let start = 0;
  let end = arr.length - 1;
  while (start < end) {
    let mid = Math.floor(start + (end - start) / 2);
    if (arr[mid] > arr[mid + 1]) end = mid;
    else start = mid + 1;
  }
  return arr[start];
};

// Time complexity for these solutions is O(log N)

// Space complexity is O(1)

console.log(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]));
console.log(find_max_in_bitonic_array([3, 8, 3, 1]));
console.log(find_max_in_bitonic_array([1, 3, 8, 12]));
console.log(find_max_in_bitonic_array([10, 9, 8]));
