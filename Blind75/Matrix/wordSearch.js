// Given an m x n grid of characters board and a string word, return true if word exists in the grid.

// The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

// Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
// Output: true

// Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
// Output: true

var exist = function (board, word) {
  let height = board.length;
  let width = board[0].length;

  for (let i = 0; i < height; i++) {
    for (let j = 0; j < width; j++) {
      if (board[i][j] === word[0] && dfs(board, word, 0, i, j)) {
        return true;
      }
    }
  }
  return false;
};

let dfs = function (board, word, index, i, j) {
  if (index === word.length) {
    return true;
  }

  if (
    i < 0 ||
    i >= board.length ||
    j < 0 ||
    j >= board[i].length ||
    board[i][j] !== word[index]
  ) {
    return false;
  }

  let temp = board[i][j];
  board[i][j] = ' ';
  let found =
    dfs(board, word, index + 1, i - 1, j) ||
    dfs(board, word, index + 1, i + 1, j) ||
    dfs(board, word, index + 1, i, j - 1) ||
    dfs(board, word, index + 1, i, j + 1);

  board[i][j] = temp;
  return found;
};

// Time complexity is O(n)

// Space complexity is O(n)
