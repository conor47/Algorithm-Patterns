// There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to print all possible ordering of tasks meeting all prerequisites.

// Example 1:

// Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
// Output: [0, 1, 2]
// Explanation: There is only possible ordering of the tasks.

// Example 2:

// Input: Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1]
// Output:
// 1) [3, 2, 0, 1]
// 2) [3, 2, 1, 0]
// Explanation: There are two possible orderings of the tasks meeting all prerequisites.

// Example 3:

// Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
// Output:
// 1) [0, 1, 4, 3, 2, 5]
// 2) [0, 1, 3, 4, 2, 5]
// 3) [0, 1, 3, 2, 4, 5]
// 4) [0, 1, 3, 2, 5, 4]
// 5) [1, 0, 3, 4, 2, 5]
// 6) [1, 0, 3, 2, 4, 5]
// 7) [1, 0, 3, 2, 5, 4]
// 8) [1, 0, 4, 3, 2, 5]
// 9) [1, 3, 0, 2, 4, 5]
// 10) [1, 3, 0, 2, 5, 4]
// 11) [1, 3, 0, 4, 2, 5]
// 12) [1, 3, 2, 0, 5, 4]
// 13) [1, 3, 2, 0, 4, 5]

const print_orders = function (tasks, prerequisites) {
  const sorted = [];

  if (tasks <= 0) return sorted;

  const inDegree = Array(tasks).fill(0);

  const graph = Array(tasks)
    .fill(0)
    .map(() => Array());

  for (let [v, e] of prerequisites) {
    graph[v].push(e);
    inDegree[e] += 1;
  }

  const sources = [];

  for (let i = 0; i < inDegree.length; i++) {
    if (inDegree[i] === 0) {
      sources.push(i);
    }
  }

  print_all(graph, inDegree, sources, sorted);
};

const print_all = function (graph, inDegree, sources, sorted) {
  if (sources.length > 0) {
    for (let i = 0; i < sources.length; i++) {
      let vertex = sources[i];
      sorted.push(vertex);

      //   create a copy of the sources for the next call and remove the current source
      const sourcesForNextCall = sources.slice(0);
      sourcesForNextCall.splice(sourcesForNextCall.indexOf(vertex), 1);

      graph[vertex].forEach((child) => {
        inDegree[child]--;
        if (inDegree[child] === 0) {
          sourcesForNextCall.push(child);
        }
      });

      print_all(graph, inDegree, sourcesForNextCall, sorted);

      //   backtrack. Remove the current source from the sorted order and re add all of its children to consider the next source
      sorted.splice(sorted.indexOf(vertex), 1);
      for (let p = 0; p < graph[vertex].length; p++) {
        inDegree[graph[vertex][p]] += 1;
      }
    }
  }

  //   if sorted order does not contain all tasks then either we have a cyclic dependency between tasks or we have not processed all tasks
  // in the current recursive call
  if (sorted.length === inDegree.length) {
    console.log(sorted);
  }
};

console.log('Task Orders: ');
print_orders(3, [
  [0, 1],
  [1, 2],
]);

console.log('Task Orders: ');
print_orders(4, [
  [3, 2],
  [3, 0],
  [2, 0],
  [2, 1],
]);

console.log('Task Orders: ');
print_orders(6, [
  [2, 5],
  [0, 5],
  [0, 4],
  [1, 4],
  [3, 2],
  [1, 3],
]);
