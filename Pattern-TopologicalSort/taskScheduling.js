// There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.

// Example 1:

// Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
// Output: true
// Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs
// to finish before '2' can be scheduled. One possible scheduling of tasks is: [0, 1, 2]

// Example 2:

// Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
// Output: false
// Explanation: The tasks have a cyclic dependency, therefore they cannot be scheduled.

// Example 3:

// Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
// Output: true
// Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5]

const Deque = require('collections/deque');

const is_scheduling_possible = function (tasks, prerequisites) {
  const result = [];

  const indegree = new Array(tasks).fill(0);

  const graph = new Array(tasks).fill(0).map(() => new Array());
  for (let [v, e] of prerequisites) {
    graph[v].push(e);
    indegree[e] += 1;
  }

  const sources = new Deque();
  for (let i = 0; i < indegree.length; i++) {
    if (indegree[i] === 0) {
      sources.push(i);
    }
  }
  while (sources.length) {
    let vertice = sources.shift();
    result.push(vertice);
    graph[vertice].forEach((e) => {
      indegree[e] -= 1;
      if (indegree[e] === 0) {
        sources.push(e);
      }
    });
  }

  return result.length === tasks;
};

// Time complexity is O(V + E) since vertice can become a source only once and each edge will be removed only once

// Space complexity is O(V + E) since we are storing an adjaceny list representation of the graph

console.log(
  `Is scheduling possible: ${is_scheduling_possible(3, [
    [0, 1],
    [1, 2],
  ])}`
);
console.log(
  `Is scheduling possible: ${is_scheduling_possible(3, [
    [0, 1],
    [1, 2],
    [2, 0],
  ])}`
);
console.log(
  `Is scheduling possible: ${is_scheduling_possible(6, [
    [0, 4],
    [1, 4],
    [3, 2],
    [1, 3],
  ])}`
);
