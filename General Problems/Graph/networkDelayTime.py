# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for u,v,w in times:
            graph[u].append((v,w))
        
        distance = {node:float('inf') for node in range(1,n+1)}
        
        seen = [False] * (n+1)
        
        distance[k] = 0
        
        while True:
            cand_node = -1
            cand_distance = float('inf')
            
            for i in range(1,n+1):
                if not seen[i] and distance[i] < cand_distance:
                    cand_distance = distance[i]
                    cand_node = i
            
            if cand_node < 0:
                break
            seen[cand_node] = True
            
            for neighbour,d in graph[cand_node]:
                distance[neighbour] = min(distance[neighbour],distance[cand_node] + d)
                
        ans = max(distance.values())
        return ans if ans < float('inf') else -1