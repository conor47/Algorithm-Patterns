# There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

# Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

# Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

# Dijkstras algorithm. BFS and DFS are actually unsuitable for this problem

import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for u,v,weight in edges:
            graph[u].append((v,weight))
            graph[v].append((u,weight))
        
        def dijkstra(city):
            heap = [(0,city)]
            dist = {}
            
            while heap:
                d,u = heapq.heappop(heap)
                if u in dist:
                    continue
                if u != city:
                     dist[u] = weight + d
                for v,weight in graph[u]:
                    if v in dist:
                        continue
                    if weight + d <= distanceThreshold:
                        heapq.heappush(heap,(weight+d,v))
                       
            return len(dist)
            
        return max([(dijkstra(city),city) for city in range(n)], key=lambda x:(-x[0],x[1]))[-1]

