// You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

// Return true if the edges of the given graph make up a valid tree, and false otherwise.

// Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
// Output: true

var validTree = function (n, edges) {
  let adjacencyList = new Array(n).fill(0).map(() => new Array());

  for (const edge of edges) {
    adjacencyList[edge[0]].push(edge[1]);
    adjacencyList[edge[1]].push(edge[0]);
  }

  let stack = [0];
  let parent = new Map();
  parent.set(0, -1);

  while (stack.length) {
    let node = stack.pop();

    for (let neighbour of adjacencyList[node]) {
      if (parent.get(node) === neighbour) {
        continue;
      }

      if (parent.has(neighbour)) {
        return false;
      }

      stack.push(neighbour);
      parent.set(neighbour, node);
    }
  }
  return parent.size === n;
};

// Time complexity is O(N + E) where N is the number of nodes and E is the number of edges. Constructing the adjacency matrix takes O(N + E)
// time and then performing the DFS takes O(N + E) time

// Space comlexity is complexity is O(N + E) for the adjacency list. The max stack size is also O(N)
