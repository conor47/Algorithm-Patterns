class UnionFind:

    def __init__ (self,size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self,x):
        while x != self.root[x]:
            x = self.root[x]
        return x
    
    def union(self,x,y):
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
    
    def connected(self,x,y):
        return self.find(x) == self.find(y)

# The find operation takes O(Log N) time

# The union and connected operations rely on the find operation and so take O(Log N) time

