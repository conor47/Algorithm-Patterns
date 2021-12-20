# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

# It's guaranteed that each city can reach city 0 after reorder.

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = set()
        graph = defaultdict(list)
        self.res = 0
        
        for u,v in connections:
            roads.add((u,v))
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(node,parent):
            self.res += (parent,node) in roads
            
            for nei in graph[node]:
                if nei == parent:
                    continue
                dfs(nei,node)
            
        dfs(0,-1)
        return self.res

# Time complexity is O(V + E)

# Space complexity is O(N)