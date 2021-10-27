// Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

// Example 1:

// Input: [4, 1, 2, -1, 1, -3], target=1
// Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
// Explanation: Both the quadruplets add up to the target.

// Example 2:

// Input: [2, 0, -1, 1, -2, 2], target=2
// Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
// Explanation: Both the quadruplets add up to the target.

const search_quadruplets = function (arr, target) {
  const quadruplets = [];
  arr.sort((a, b) => a - b);
  for (let i = 0; i < arr.length - 3; i++) {
    if (i > 0 && arr[i] === arr[i - 1]) continue;

    for (let j = i + 1; j < arr.length - 2; j++) {
      if (j > i + 1 && arr[j] === arr[j - 1]) continue;

      searchPair(arr, target, i, j, quadruplets);
    }
  }

  return quadruplets;
};

const searchPair = function (arr, target, first, second, quadruplets) {
  let left = second + 1;
  let right = arr.length - 1;

  while (left < right) {
    //   we find a match
    let sum = arr[first] + arr[second] + arr[left] + arr[right];
    if (sum === target) {
      quadruplets.push([arr[first], arr[second], arr[left], arr[right]]);
      left += 1;
      right -= 1;

      while (left < right && arr[left] === arr[left - 1]) {
        left += 1;
      }

      while (left < right && arr[right] === arr[right + 1]) {
        right -= 1;
      }
    }
    // we do not find a match
    else if (sum < target) {
      left += 1;
    } else {
      right -= 1;
    }
  }
};

// Time complexity is O(N^3). Time complexity for sorting the array is O(N * Log n). Time complexity of searching for for matches is O(N^3)

// Space complexity is O(N). Required for sorting

console.log(search_quadruplets([4, 1, 2, -1, 1, -3], 1));
console.log(search_quadruplets([2, 0, -1, 1, -2, 2], 2));
