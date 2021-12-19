# There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

# A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node.

# Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        WHITE,GREY,BLACK = 0,1,2
        color = defaultdict(int)
        
        def dfs(node):
            if color[node] != WHITE:
                return color[node] == BLACK
            
            color[node] = GREY
            for nei in graph[node]:
                if color[nei] == BLACK:
                    continue
                if color[nei] == GREY or not dfs(nei):
                    return False
            color[node] = BLACK
            return True
        
        return filter(dfs,range(len(graph)))

# Time complexity is O( N + E )
# Space complexity is O(N)