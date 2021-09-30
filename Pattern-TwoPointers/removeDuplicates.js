// Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

// Example 1:

// Input: [2, 3, 3, 3, 6, 9, 9]
// Output: 4
// Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

// Example 2:

// Input: [2, 2, 2, 11]
// Output: 2
// Explanation: The first two elements after removing the duplicates will be [2, 11].

function removeDuplicates(arr) {
  let left = 0;
  let right = 1;

  while (right < arr.length) {
    if (arr[right] === arr[left]) {
      arr.splice(right, 1);
      continue;
    }
    left = right;
    right += 1;
  }
  return arr.length;
}

// solution where the resultant length of the array remains the same

function removeDuplicatesV2(arr) {
  let nextNonDuplicate = 1;

  let i = 1;
  while (i < arr.length) {
    if (arr[nextNonDuplicate] - 1 !== arr[i]) {
      arr[nextNonDuplicate] = arr[i];
      nextNonDuplicate += 1;
    }
    i += 1;
  }
  return nextNonDuplicate;
}

// time complexity is O(N) where N is the number of elements in the array

// Space complexity is O(1)
