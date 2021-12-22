# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * n
        for u,v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        res = []
        for i in range(n):
            if indegree[i] == 0:
                res.append(i)
        return res

# Time complexity is O(V + E)

# Space complexity is O(V + E)