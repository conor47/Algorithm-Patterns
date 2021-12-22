# You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

# Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

# If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for (u,v),w in zip(edges,succProb):
            graph[u].append((v,w))
            graph[v].append((u,w))
        
        heap = [(-1,start)]
        seen = set()
        while heap:
            prob,node = heapq.heappop(heap)
            if node == end:
                return -prob
            seen.add(node)
            for nei,w in graph[node]:
                if nei in seen:
                    continue
                heapq.heappush(heap,(prob * w, nei))
        return 0

# Time complexity is O(V^2) since we are using dijkstra but using a minheap reduces it to O(V + ELogV)

# Space complexity is O(V + E)