// Given a sequence originalSeq and an array of sequences, write a method to find if originalSeq can be uniquely reconstructed from the array of sequences.

// Unique reconstruction means that we need to find if originalSeq is the only sequence such that all sequences in the array are subsequences of it.

// Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [3, 4]]
// Output: true
// Explanation: The sequences [1, 2], [2, 3], and [3, 4] can uniquely reconstruct
// [1, 2, 3, 4], in other words, all the given sequences uniquely define the order of numbers
// in the 'originalSeq'.

// Example 2:

// Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [2, 4]]
// Output: false
// Explanation: The sequences [1, 2], [2, 3], and [2, 4] cannot uniquely reconstruct
// [1, 2, 3, 4]. There are two possible sequences we can construct from the given sequences:
// 1) [1, 2, 3, 4]
// 2) [1, 2, 4, 3]

// Example 3:

// Input: originalSeq: [3, 1, 4, 2, 5], seqs: [[3, 1, 5], [1, 4, 2, 5]]
// Output: true
// Explanation: The sequences [3, 1, 5] and [1, 4, 2, 5] can uniquely reconstruct
// [3, 1, 4, 2, 5].
const Dequeue = require('collections/deque');

const can_construct = function (originalSeq, sequences) {
  const sorted = [];
  const inDegree = {};
  const graph = {};

  sequences.forEach((sequence) => {
    for (let i = 0; i < sequence.length; i++) {
      inDegree[sequence[i]] = 0;
      graph[sequence[i]] = [];
    }
  });

  sequences.forEach((sequence) => {
    for (let i = 1; i < sequence.length; i++) {
      let parent = sequence[i - 1];
      let child = sequence[i];
      inDegree[child] += 1;
      graph[parent].push(child);
    }
  });

  //   if we do not have ordering rules for all numbers then we cannot construct a
  // unique sequence
  const vertices = Object.keys(inDegree);
  if (vertices.length !== originalSeq.length) {
    return false;
  }

  const sources = new Dequeue();
  vertices.forEach((key) => {
    if (inDegree[key] === 0) {
      sources.push(key);
    }
  });

  while (sources.length > 0) {
    if (sources.length > 1) {
      return false;
    }

    let source = sources.shift();
    sorted.push(source);
    graph[source].forEach((child) => {
      inDegree[child] -= 1;
      if (inDegree[child] === 0) {
        sources.push(child);
      }
    });
  }
  return sorted.length === originalSeq.length;
};

console.log(
  `Can construct: ${can_construct(
    [1, 2, 3, 4],
    [
      [1, 2],
      [2, 3],
      [3, 4],
    ]
  )}`
);
console.log(
  `Can construct: ${can_construct(
    [1, 2, 3, 4],
    [
      [1, 2],
      [2, 3],
      [2, 4],
    ]
  )}`
);
console.log(
  `Can construct: ${can_construct(
    [3, 1, 4, 2, 5],
    [
      [3, 1, 5],
      [1, 4, 2, 5],
    ]
  )}`
);
