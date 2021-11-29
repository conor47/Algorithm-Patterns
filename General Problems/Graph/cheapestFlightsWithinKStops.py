# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0
        seen = defaultdict(lambda:float('inf'))
        graph = defaultdict(list)
        
        for u,v,w in flights:
            graph[u] += [(v,w)]
        
        q = [(src,-1,0)]
        
        while q:
            pos,stops,cost = q.pop(0)
            if stops == k or pos == dst:
                continue
            
            for nei,c in graph[pos]:
                if cost + c < seen[nei]:
                    seen[nei] = cost + c
                    q.append((nei,stops+1,cost+c))
                    
        return seen[dst] if seen[dst] < float('inf') else -1 

# Time complexity is O(E * K) since we can process each edge multiple times however the number of times is bounded by k

# Space complexity is O(V^2 + V * K). The first part is the stsandard space complexity of an adjacency matrix representation of a graph.
# The second part is for the seen dictionary