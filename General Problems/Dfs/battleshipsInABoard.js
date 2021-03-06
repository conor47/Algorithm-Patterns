// Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

// Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

// Constraints:

//     m == board.length
//     n == board[i].length
//     1 <= m, n <= 200
//     board[i][j] is either '.' or 'X'.

// first solution using depth first search

const countBattleships = function (board) {
  let ships = 0;
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[0].length; j++) {
      if (board[i][j] === 'X') {
        ships += 1;
        dfs(board, i, j);
      }
    }
  }
  return ships;
};

const dfs = function (board, i, j) {
  if (
    i < 0 ||
    i >= board.length ||
    j < 0 ||
    j >= board[0].length ||
    board[i][j] !== 'X'
  ) {
    return;
  }

  board[i][j] = '.';
  dfs(board, i + 1, j);
  dfs(board, i - 1, j);
  dfs(board, i, j + 1);
  dfs(board, i, j - 1);
};

// Time complexity is O(N * M)

// Space complexity is O(max(N, M))

// One pass solution using O(1) memory and without modifying the board

const countBattleshipsV2 = function (board) {
  let ships = 0;
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[0].length; j++) {
      if (board[i][j] === '.') {
        continue;
      }
      if (i > 0 && board[i - 1][j] === 'X') {
        continue;
      }

      if (j > 0 && board[i][j - 1] === 'X') {
        continue;
      }
      ships += 1;
    }
  }
  return ships;
};

// Time complexity is O(N * M)
