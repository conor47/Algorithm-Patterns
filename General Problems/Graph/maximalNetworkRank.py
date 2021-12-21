# There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

# The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

# The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

# Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in roads:
            graph[u].append((u,v))
            graph[v].append((v,u))
        
        maxRank = 0
        for i in range (n-1):
            for j in range(i+1,n):
                roads = set(graph[i])
                for road in graph[j]:
                    if road[::-1] not in roads:
                        roads.add(road)
                maxRank = max(maxRank,len(roads))
        return maxRank

# Time complexity is O(N^2)

# Space complexity is O(V + E)

# Another solution, time complexity is still O(N^2) but runs faster and has lower memory 
# overhead

import collections
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connected = collections.defaultdict(set)
        for a, b in roads:
            connected[a].add(b)
            connected[b].add(a)
        M = 0
        for i in range(n):
            for j in range(i + 1, n):
                M = max(M, len(connected[i]) + len(connected[j]) - (i in connected[j]))
        return M