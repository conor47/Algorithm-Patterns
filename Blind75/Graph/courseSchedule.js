// There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

//     For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

// Return true if you can finish all courses. Otherwise, return false.

// Example 1:

// Input: numCourses = 2, prerequisites = [[1,0]]
// Output: true
// Explanation: There are a total of 2 courses to take.
// To take course 1 you should have finished course 0. So it is possible.

// Example 2:

// Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
// Output: false
// Explanation: There are a total of 2 courses to take.
// To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

// Constraints:

//     1 <= numCourses <= 105
//     0 <= prerequisites.length <= 5000
//     prerequisites[i].length == 2
//     0 <= ai, bi < numCourses
//     All the pairs prerequisites[i] are unique.

let graph;
let visited;
let visiting;

var canFinish = function (numCourses, prerequisites) {
  graph = new Map();
  visiting = new Set();
  visited = new Set();

  for (let [v, e] of prerequisites) {
    if (graph.has(v)) {
      let edges = graph.get(v);
      edges.push(e);
      graph.set(v, edges);
    } else {
      graph.set(v, [e]);
    }
  }

  for (const [v, e] of graph) {
    if (DFS(v)) {
      return false;
    }
  }

  return true;
};

const DFS = function (v) {
  visiting.add(v);
  let edges = graph.get(v);

  if (edges) {
    for (let e of edges) {
      if (visited.has(e)) {
        continue;
      }

      if (visiting.has(e)) {
        return true;
      }

      if (DFS(e)) {
        return true;
      }
    }
  }

  visiting.delete(v);
  visited.add(v);
  return false;
};

// Time complexity is O(V + E)

// Space complexity is O(V + E) for the graph. The additional data structures
// also consume space but are bounded by O(V). In the worst case the recursion stack
// would take O(V) space.
