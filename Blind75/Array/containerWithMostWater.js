// Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

// Notice that you may not slant the container.

// Input: height = [1,8,6,2,5,4,8,3,7]
// Output: 49
// Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

// Example 2:

// Input: height = [1,1]
// Output: 1

// Example 3:

// Input: height = [4,3,2,1,4]
// Output: 16

// Example 4:

// Input: height = [1,2,1]
// Output: 2

// Constraints:

//     n == height.length
//     2 <= n <= 105
//     0 <= height[i] <= 104

// Naive solution

let maxArea = function (height) {
  let maxArea = Number.MIN_VALUE;

  for (let i = 0; i < height.length - 1; i++) {
    for (let j = i + 1; j <= height.length - 1; j++) {
      let min = Math.min(height[i], height[j]);
      maxArea = Math.max(maxArea, min * (j - i));
    }
  }
  return maxArea;
};

// Time complexity is O(n^2)

// Space complexity is O(1)

// sliding window implementation

var maxArea = function (height) {
  let maxArea = Number.MIN_VALUE;

  let i = 0;
  let j = height.length - 1;

  while (i < j) {
    let min = Math.min(height[i], height[j]);
    maxArea = Math.max(maxArea, min * (j - i));

    if (height[j] < height[i]) {
      j -= 1;
    } else {
      i += 1;
    }
  }
  return maxArea;
};

// Time complexity is O(N)

// Space complexity is O(1)
