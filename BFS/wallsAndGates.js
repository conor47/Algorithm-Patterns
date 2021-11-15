// You are given an m x n grid rooms initialized with these three possible values.

//     -1 A wall or an obstacle.
//     0 A gate.
//     INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

// Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

// Here is a BFS solution

const GATE = 0;
const DIRS = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];
const EMPTY = 2147483647;

const inbound = function (arr, i, j) {
  return i >= 0 && i < arr.length && j >= 0 && j < arr[0].length;
};

const wallsAndGates = function (rooms) {
  if (rooms.length === 0) return;
  const m = rooms.length;
  const n = rooms[0].length;

  let queue = [];

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (rooms[i][j] === GATE) {
        queue.push([i, j]);
      }
    }
  }

  while (queue.length) {
    const [gateRow, gateCol] = queue.shift();

    for (let [dx, dy] of DIRS) {
      let r = gateRow + dx;
      let c = gateCol + dy;

      if (!inbound(rooms, r, c) || rooms[r][c] !== EMPTY) {
        continue;
      }

      rooms[r][c] = rooms[gateRow][gateCol] + 1;
      queue.push([r, c]);
    }
  }
};

// Time complexity is O(M * N)

// Space complexity is O(M * N)

// Here is a conceptually simpler DFS solution that times out on Leetcode

const wallsAndGatesV2 = function (rooms) {
  for (let i = 0; i < rooms.length; i++) {
    for (let j = 0; j < rooms[0].length; j++) {
      if (rooms[i][j] === 0) {
        dfs(rooms, i, j, 0);
      }
    }
  }
  return rooms;
};

const dfs = function (rooms, i, j, count) {
  if (
    i < 0 ||
    i >= rooms.length ||
    j < 0 ||
    j >= rooms[0].length ||
    rooms[i][j] < count
  ) {
    return;
  }
  rooms[i][j] = count;
  dfs(rooms, i + 1, j, count + 1);
  dfs(rooms, i - 1, j, count + 1);
  dfs(rooms, i, j + 1, count + 1);
  dfs(rooms, i, j - 1, count + 1);
};
