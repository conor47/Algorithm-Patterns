// There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

// You want to determine if there is a valid path that exists from vertex start to vertex end.

// Given edges and the integers n, start, and end, return true if there is a valid path from start to end, or false otherwise.

// Input: n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2
// Output: true
// Explanation: There are two paths from vertex 0 to vertex 2:
// - 0 → 1 → 2
// - 0 → 2

// Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], start = 0, end = 5
// Output: false
// Explanation: There is no path from vertex 0 to vertex 5.

// Constraints:

//     1 <= n <= 2 * 105
//     0 <= edges.length <= 2 * 105
//     edges[i].length == 2
//     0 <= ui, vi <= n - 1
//     ui != vi
//     0 <= start, end <= n - 1
//     There are no duplicate edges.
//     There are no self edges.

const validPath = function (n, edges, start, end) {
  let visited = Array(n).fill(false);
  let graph = new Map();
  let i, j;

  for (i = 0; i < n; i++) {
    graph.set(i, new Map());
  }

  for (let i of edges) {
    graph.get(i[0]).set(i[1], true);
    graph.get(i[1]).set(i[0], true);
    if (graph.get(start).has(end)) {
      return true;
    }
  }

  seen = false;

  let dfs = function (graph, visited, start, end) {
    if (!visited[start] && !seen) {
      if (start === end) {
        seen = true;
        return;
      }

      visited[start] = true;

      for (let key of graph.get(start).keys()) {
        dfs(graph, visited, key, end);
      }
    }
  };
  dfs(graph, visited, start, end);
  return seen;
};
