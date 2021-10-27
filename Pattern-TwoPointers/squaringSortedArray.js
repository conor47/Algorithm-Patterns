// Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

// Example 1:

// Input: [-2, -1, 0, 2, 3]
// Output: [0, 1, 4, 4, 9]

// Example 2:

// Input: [-3, -1, 0, 1, 2]
// Output: [0, 1, 1, 4, 9]

function squareSorted(arr) {
  let n = arr.length;
  let squares = Array(n).fill(0);
  let highestIdx = n - 1;
  let left = 0;
  let right = n - 1;

  while (left <= right) {
    let leftSquare = arr[left] * arr[left];
    let rightSquare = arr[right] * arr[right];
    if (leftSquare > rightSquare) {
      squares[highestIdx] = leftSquare;
      left += 1;
    } else {
      squares[highestIdx] = rightSquare;
      right -= 1;
    }
    highestIdx -= 1;
  }

  return squares;
}

// Time complexity is O(N)

// Space complexity is O(N)

console.log(squareSorted([-3, -1, 0, 1, 2]));
