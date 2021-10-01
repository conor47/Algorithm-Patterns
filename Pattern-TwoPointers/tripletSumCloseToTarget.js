// Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

// Example 1:

// Input: [-2, 0, 1, 2], target=2
// Output: 1
// Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

// Example 2:

// Input: [-3, -1, 1, 2], target=1
// Output: 0
// Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

// Example 3:

// Input: [1, 0, 1, 1], target=100
// Output: 3
// Explanation: The triplet [1, 1, 1] has the closest sum to the target.

function uniqueTriplets(arr, target) {
  arr.sort((a, b) => a - b);
  let smallestDifference = Infinity;

  for (let i = 0; i < arr.length - 2; i++) {
    let left = i + 1;
    let right = arr.length - 1;

    while (left < right) {
      let targetDifference = target - arr[i] - arr[left] - arr[right];
      if (targetDifference === 0) {
        return target - targetDifference;
      }

      if (Math.abs(targetDifference) < Math.abs(smallestDifference)) {
        smallestDifference = targetDifference;
      }

      if (
        Math.abs(targetDifference) < Math.abs(smallestDifference) ||
        // this second condition handles the situation where we have more than one solution. We return the smallest sum
        (Math.abs(targetDifference) === Math.abs(smallestDifference) &&
          targetDifference > smallestDifference)
      ) {
        smallestDifference = targetDifference;
      }

      if (targetDifference > 0) {
        left += 1;
      } else {
        right -= 1;
      }
    }
  }

  return targetSum - smallestDifference;
}

// sorting the array takes O(N * LogN time). Overall the algorithm will take O(N * LogN + N^2) which is asymptotically equivalent
// to O(N^2)

// space complexity is O(N) which is required for sorting
