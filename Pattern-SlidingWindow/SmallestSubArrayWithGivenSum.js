// Given an array of positive numbers and a positive number āS,ā find the length of the smallest contiguous subarray whose
//  sum is greater than or equal to āSā. Return 0 if no such subarray exists.

// Example 1:

// Input: [2, 1, 5, 2, 3, 2], S=7
// Output: 2
// Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].

// Example 2:

// Input: [2, 1, 5, 2, 8], S=7
// Output: 1
// Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

// Example 3:

// Input: [3, 4, 1, 1, 6], S=8
// Output: 3
// Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1]
// or [1, 1, 6].

function SmallestSubarray(arr, s) {
  let smallest = Infinity;
  let windowStart = 0;
  let windowSum = 0;

  for (let windowEnd = 0; windowEnd < arr.length; windowEnd++) {
    windowSum += arr[windowEnd];

    while (windowSum >= s) {
      smallest = Math.min(smallest, windowEnd - windowStart + 1);
      windowSum -= arr[windowStart];
      windowStart += 1;
    }
  }

  return smallest === Infinity ? 0 : smallest;
}

const result = SmallestSubarray([2, 1, 5, 2, 8], 7);
console.log(result);

// Time complexity is O(N + N) which asymptotically is O(N)
