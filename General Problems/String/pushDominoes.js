// There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

// After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

// When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

// For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

// You are given a string dominoes representing the initial state where:

//     dominoes[i] = 'L', if the ith domino has been pushed to the left,
//     dominoes[i] = 'R', if the ith domino has been pushed to the right, and
//     dominoes[i] = '.', if the ith domino has not been pushed.

// Return a string representing the final state.

// Example 1:

// Input: dominoes = "RR.L"
// Output: "RR.L"
// Explanation: The first domino expends no additional force on the second domino.

var pushDominoes = function (dominoes) {
  let chars = dominoes.split('');

  let forces = Array(chars.length).fill(0);
  let n = chars.length;

  let force = 0;
  for (let i = 0; i < chars.length; i++) {
    if (chars[i] === 'R') {
      force = n;
    } else if (chars[i] === 'L') {
      force = 0;
    } else {
      force = Math.max(force - 1, 0);
    }
    forces[i] = +force;
  }

  force = 0;
  for (let i = n - 1; i >= 0; i--) {
    if (chars[i] === 'L') {
      force = n;
    } else if (chars[i] === 'R') {
      force = 0;
    } else {
      force = Math.max(force - 1, 0);
    }
    forces[i] -= force;
  }
  for (let i = 0; i < n; i++) {
    if (forces[i] === 0) {
      chars[i] = '.';
    } else if (forces[i] > 0) {
      chars[i] = 'R';
    } else {
      chars[i] = 'L';
    }
  }
  return chars.join('');
};

// Time complexity is O(N)

// Space complexity is O(N)
