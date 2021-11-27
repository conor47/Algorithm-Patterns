# Given the edges of a directed graph where edges[i] = [ai, bi] indicates there is an edge between nodes ai and bi, and two nodes source and destination of this graph, determine whether or not all paths starting from source eventually, end at destination, that is:

#     At least one path exists from the source node to the destination node
#     If a path exists from the source node to a node with no outgoing edges, then that node is equal to destination.
#     The number of possible paths from source to destination is a finite number.

# Return true if and only if all roads from source lead to destination.

class Solution:
    GRAY = 1
    BLACK = 2
    
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, target: int) -> bool:
        self.graph = [[] for _ in range(n)]
    
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
        
        return self.leadsToDest (self.graph,source,target,[None] * n)
    
    def leadsToDest(self,graph,node,dest,states):
        if states[node] != None:
            return states[node] == Solution.BLACK
        
        if len(graph[node]) == 0:
            return node == dest
        
        states[node] = Solution.GRAY
        
        for next in graph[node]:
            
            if not self.leadsToDest(self.graph,next,dest,states):
                return False
            
        states[node] = Solution.BLACK
        return True

    # Time complexity is typically O(V + E) for dfs. In the worst case E can be O(V^2) in the case that every vertice is connected to 
    # every other vertice in the graph. Due to pruning the recursion tree and backtracking the overall time complexity is reduced to 
    # O(V)

    # Space complexity is O(V + E). E is occupied by the adjacency list representation of the graph and V by the recursion stack
    # and color states of the graph