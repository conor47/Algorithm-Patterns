# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20

# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.

# Example 2:

# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18

# Example 3:

# Input: points = [[0,0],[1,1],[1,0],[-1,1]]
# Output: 4

# Example 4:

# Input: points = [[-1000000,-1000000],[1000000,1000000]]
# Output: 4000000

# Example 5:

# Input: points = [[0,0]]
# Output: 0

 

# Constraints:

#     1 <= points.length <= 1000
#     -106 <= xi, yi <= 106
#     All pairs (xi, yi) are distinct.

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        djs = UnionFind(n)
        edges = []
        for i in range(n):
            for j in range(i+1,n):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((distance,i,j))
        edges.sort()
        cost = 0
        num_edges = 0
        while num_edges <n-1:
            distance,i,j = edges.pop(0)
            if djs.union(i,j):
                cost += distance
                num_edges += 1
        return cost

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

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
            return True
        else:
            return False

    def connected(self, x, y):
        return self.find(x) == self.find(y)
