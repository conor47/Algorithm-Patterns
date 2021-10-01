// Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.

// Example 1:

// Input: [-1, 0, 2, 3], target=3
// Output: 2
// Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

// Example 2:

// Input: [-1, 4, 2, 1, 3], target=5
// Output: 4
// Explanation: There are four triplets whose sum is less than the target:
//    [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]

function smallerSum(arr, target) {
  arr.sort((a, b) => a - b);

  let count = 0;

  for (let i = 0; i < arr.length - 2; i++) {
    count += findPair(arr, target - arr[i], i);
  }

  return count;
}

function findPair(arr, targetSum, first) {
  let count = 0;
  let left = first + 1;
  let right = arr.length - 1;

  while (left < right) {
    if (arr[left] + arr[right] < targetSum) {
      //  since the arr is sorted once we find a triplet we know we can replace right with any value between left and right and the
      //  sum will still be below the target
      count += right - left;
      left += 1;
    } else {
      right -= 1;
    }
  }
  return count;
}

console.log(smallerSum([-1, 4, 2, 1, 3], 5));
