# There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

#     There are no self-edges (graph[u] does not contain u).
#     There are no parallel edges (graph[u] does not contain duplicate values).
#     If v is in graph[u], then u is in graph[v] (the graph is undirected).
#     The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.

# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

# Return true if and only if it is bipartite.

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        NOT_COLORED, BLUE, Green = 0,1,-1
        n = len(graph)
        color_table = [0] * n
        
        def helper(node,color):
            color_table[node] = color
            
            for other in graph[node]:
                if color_table[other] == color:
                    return False
                if color_table[other] == NOT_COLORED and not helper(other,-color):
                    return False
            return True
        
        for i in range(n):
            if color_table[i] == NOT_COLORED and not helper(i,BLUE):
                return False
        return True

# Time complexity is O(N + E)

# Space complexity is O(N )