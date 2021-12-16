# There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

# You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

# Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        res = [0] * n
        count = [1] * n
        tree = defaultdict(list)
        
        for i,j in edges:
            tree[i].append(j)
            tree[j].append(i)
        
        def dfs1(root,pre):
            for i in tree[root]:
                if i != pre:
                    dfs1(i,root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]
                    
        def dfs2(root,pre):
            for i in tree[root]:
                if i != pre:
                    res[i] = res[root] - count[i] + n - count[i]
                    dfs2(i,root)
        
        dfs1(0,-1)
        dfs2(0,-1)
        return res


# Time complexity is O(N)
# Space complexity is O(N)

# Intuitive BFS solution which TLEs on leetcode

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        res = [0] * n
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        def bfs(node):
            total = 0
            q = [(node,0)]
            seen = set()
            while q :
                node,dist = q.pop(0)
                total += dist
                seen.add(node)
                for nei in graph[node]:
                    if nei not in seen:
                        q.append((nei,dist+1))
            return total
        
        for i in range(n):
            res[i] = bfs(i)
        return res

# Time complexity is O(N^2)

# Space complexity is O(N)