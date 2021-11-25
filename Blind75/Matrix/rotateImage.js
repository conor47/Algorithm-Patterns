// You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

// You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

// Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
// Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

// Example 3:

// Input: matrix = [[1]]
// Output: [[1]]

// Example 4:

// Input: matrix = [[1,2],[3,4]]
// Output: [[3,1],[4,2]]

// Constraints:

//     matrix.length == n
//     matrix[i].length == n
//     1 <= n <= 20
//     -1000 <= matrix[i][j] <= 1000

var rotate = function (matrix) {
  let n = matrix.length;
  for (let i = 0; i < n; i++) {
    for (let j = i; j < n; j++) {
      let temp = matrix[i][j];
      matrix[i][j] = matrix[j][i];
      matrix[j][i] = temp;
    }
  }

  for (let i = 0; i < n; i++) {
    let start = 0;
    let end = n - 1;
    while (start < end) {
      [matrix[i][start], matrix[i][end]] = [matrix[i][end], matrix[i][start]];
      start += 1;
      end -= 1;
    }
  }
};

// Time complexity is O(N)

// Space complexity is O(1)
