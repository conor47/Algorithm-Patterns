# A class implementation of a quickfind disjoint set

class UnionFind:

    def __init__(self,size):
        self.root = [i for i in range(size)]

    def find(self,x):
        return self.root[x]

    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX
    
    def connected(self,x,y):
        return self.find(x) == self.find(y)

# find and connected methods are O(1) time

# Union method is O(N) time where N is the number of vertices in the graph
