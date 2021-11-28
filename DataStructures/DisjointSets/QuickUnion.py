# A class implementation of a quickUnion disjoint set

class UnionFind:

    def __init__ (self,size):
        self.root = [i for i in range(size)]

    def find(self,x):
        while x != self.root[x]:
            x = self.root[x]
        return x
    
    def union(self,x,y):
        
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self,x,y):
        return self.find(x) == self.find(y)

# find and union operations take O(Log N) time assuming we are always connecting the root of the shorter tree to the root of the taller tree

# connected also takes O(Log N) time as it consists of two find operations which are O(Log N) time
