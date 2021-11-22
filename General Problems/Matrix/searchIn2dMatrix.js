// Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

//     Integers in each row are sorted from left to right.
//     The first integer of each row is greater than the last integer of the previous row.

// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
// Output: true

var searchMatrix = function (matrix, target) {
  if (matrix.length === 0) return false;
  let rows = matrix.length;
  let cols = matrix[0].length;
  let start = 0;
  let end = rows * cols - 1;

  while (start <= end) {
    let mid = Math.floor(start + (end - start) / 2);
    let row = Math.floor(mid / cols);
    let col = mid % cols;
    if (matrix[row][col] === target) {
      return true;
    } else if (matrix[row][col] < target) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }
  return false;
};

// Time complexity is O(Log N)

// Space complexity is O(1)
