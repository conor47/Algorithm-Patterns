// Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

// An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

// Example 1:

// Input: grid = [
//   ["1","1","1","1","0"],
//   ["1","1","0","1","0"],
//   ["1","1","0","0","0"],
//   ["0","0","0","0","0"]
// ]
// Output: 1

// Example 2:

// Input: grid = [
//   ["1","1","0","0","0"],
//   ["1","1","0","0","0"],
//   ["0","0","1","0","0"],
//   ["0","0","0","1","1"]
// ]
// Output: 3

// Constraints:

//     m == grid.length
//     n == grid[i].length
//     1 <= m, n <= 300
//     grid[i][j] is '0' or '1'.

/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  let height = grid.length;
  let width = grid[0].length;
  if (height === 0 || width === 0) return 0;

  let numIslands = 0;

  for (let i = 0; i < height; i++) {
    for (let j = 0; j < width; j++) {
      if (grid[i][j] === '1') {
        numIslands += depthFirst(grid, i, j, width, height);
      }
    }
  }
  return numIslands;
};

let depthFirst = function (grid, i, j, width, height) {
  if (i < 0 || i >= height || j < 0 || j >= width || grid[i][j] === '0')
    return 0;
  grid[i][j] = '0';
  depthFirst(grid, i - 1, j, width, height);
  depthFirst(grid, i + 1, j, width, height);
  depthFirst(grid, i, j + 1, width, height);
  depthFirst(grid, i, j - 1, width, height);
  return 1;
};

// Time complexity is O(M * N) where m and n are the number of rows and columns in the grid

// Space complexity is O(min(M, N))
