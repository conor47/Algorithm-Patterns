// Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

// Example 1:

// Input: [-3, 0, 1, 2, -1, 1, -2]
// Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
// Explanation: There are four unique triplets whose sum is equal to zero.

// Example 2:

// Input: [-5, 2, -1, -2, 3]
// Output: [[-5, 2, 3], [-2, -1, 3]]
// Explanation: There are two unique triplets whose sum is equal to zero.

function uniqueTriplets(arr) {
  arr.sort((a, b) => a - b);
  let result = [];

  for (let i = 0; i < arr.length; i++) {
    if (i > 0 && arr[i] === arr[i - 1]) {
      continue;
    }
    searchPair(arr, -arr[i], i + 1, result);
  }

  return result;
}

function searchPair(arr, targetSum, left, result) {
  let right = arr.length - 1;

  while (left < right) {
    let currentSum = arr[left] + arr[right];
    if (currentSum === targetSum) {
      result.push([-targetSum, arr[left], arr[right]]);
      left += 1;
      right -= 1;

      //   skip the same element to avoid duplicate triplet
      while (left < right && arr[left] === arr[left - 1]) {
        left += 1;
      }

      //   skip the same element to avoid duplicate triplet
      while (left < right && arr[right] === arr[right + 1]) {
        right -= 1;
      }
    } else if (targetSum > currentSum) {
      left += 1;
    } else {
      right -= 1;
    }
  }
}

console.log(uniqueTriplets([-5, 2, -1, -2, 3]));
