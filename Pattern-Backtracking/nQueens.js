// The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

// Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

// Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

const solveNQueens = function (n) {
  let result = [];
  nQueens(n, 0, [], result);
  return result;
};

const nQueens = function (n, row, colPlacements, result) {
  if (row === n) {
    let board = generateBoard(n, colPlacements);
    result.push(board);
    return;
  } else {
    for (let col = 0; col < n; col++) {
      colPlacements.push(col);
      if (isValid(colPlacements)) {
        nQueens(n, row + 1, colPlacements, result);
      }
      colPlacements.pop();
    }
  }
};

const isValid = function (colPlacements) {
  let rowId = colPlacements.length - 1;
  for (let i = 0; i < rowId; i++) {
    let diff = Math.abs(colPlacements[i] - colPlacements[rowId]);
    if (diff === 0 || diff === rowId - i) {
      return false;
    }
  }
  return true;
};

function generateBoard(n, colPlacements) {
  let board = [];
  // make row for every queen in placements
  for (let row = 0; row < colPlacements.length; row++) {
    let board_row = [];
    for (let col = 0; col < n; col++) {
      if (col === colPlacements[row]) {
        board_row.push('Q');
      } else {
        board_row.push('.');
      }
    }
    board.push(board_row.join(''));
  }
  return board;
}
