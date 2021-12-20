# There are n cities labeled from 1 to n. You are given the integer n and an array connections where connections[i] = [xi, yi, costi] indicates that the cost of connecting city xi and city yi (bidirectional connection) is costi.

# Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. If it is impossible to connect all the n cities, return -1,

# The cost is the sum of the connections' costs used.

import heapq

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        djs = UnionFind(n)
        minHeap = []
        for u,v,weight in connections:
            heapq.heappush(minHeap,(weight,u-1,v-1))
        
        cost = 0
        while minHeap:
            if djs.count == 1:
                return cost
            weight,u,v = heapq.heappop(minHeap)
            
            if djs.union(u,v):
                cost += weight
        if djs.count == 1:
            return cost
        return -1
        
# Standard Union find code

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = len(self.root)

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1
            return True
        else:
            return False
        

    def connected(self, x, y):
        return self.find(x) == self.find(y)

# Time complexity is O(N) where N is the number of connections or edges in the graph

# Space complexity is O(N)