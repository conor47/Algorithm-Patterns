// ou have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

// Return the number of connected components in the graph.

// Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
// Output: 1

 

// Constraints:

//     1 <= n <= 2000
//     1 <= edges.length <= 5000
//     edges[i].length == 2
//     0 <= ai <= bi < n
//     ai != bi
//     There are no repeated edges.


// var countComponents = function(n, edges) {
//     let components = 0;
//     let visited = new Array(n).fill(0);
//     let adjacency = new Array(n).fill(0).map(() => new Array())
    
//     for(let edge of edges){
//         adjacency[edge[0]].push(edge[1])
//         adjacency[edge[1]].push(edge[0])
//     }
    
//     for(let i=0; i<n; i++){
//         if(visited[i] === 0){
//             components += 1;
//             dfs(adjacency, visited,i)
//         }
//     }
//     return components
// };

// const dfs = function(adjacency, visited, startNode){
//     visited[startNode] = 1
    
//     for(let i=0; i<adjacency[startNode].length; i++){
//         if(visited[adjacency[startNode][i]] === 0){
//             dfs(adjacency, visited, adjacency[startNode][i])
//         }
//     }
}