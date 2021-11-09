// Given an m x n matrix, return all elements of the matrix in spiral order.

var spiralOrder = function (matrix) {
  if (matrix.length === 0 || matrix[0].length === 0) return [];

  let result = [];
  let top = 0;
  let right = matrix[0].length - 1;
  let bottom = matrix.length - 1;
  let left = 0;
  let size = matrix.length * matrix[0].length;

  while (result.length < size) {
    for (let i = left; i <= right && result.length < size; i++) {
      result.push(matrix[top][i]);
    }
    top += 1;

    for (let i = top; i <= bottom && result.length < size; i++) {
      result.push(matrix[i][right]);
    }
    right -= 1;

    for (let i = right; i >= left && result.length < size; i--) {
      result.push(matrix[bottom][i]);
    }
    bottom -= 1;

    for (let i = bottom; i >= top && result.length < size; i--) {
      result.push(matrix[i][left]);
    }
    left += 1;
  }
  return result;
};

// Time complexity is O(M *N) the size of the input matrix

// Space complexity is O(1)
