# iven the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

# You can return the answer in any order.

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = {} 
        self.dfs(root,-1, graph)
        
        if target.val not in graph:
            return []
        res = []
        seen = set()
        q = [(target.val, 0)]
        while q:
            head, steps = q.pop(0)
            if head in seen:
                continue
            seen.add(head)
            if steps == k and head > -1:
                res.append(head)
            elif steps <= k:
                if head in graph:
                    children = graph[head]
                    for child in children:
                        q.append((child,steps + 1))
        return res        
        
          
        
         
    def dfs (self, node,parent, graph):
        if node is None:
            return
        
        arr = [parent,-1,-1]    
        if node.left:
            arr[1] = node.left.val
            self.dfs(node.left, node.val, graph)
        if node.right:
            arr[2] = node.right.val
            self.dfs(node.right, node.val, graph)
        graph[node.val] = arr

# Time complexity is O(N) since we are doing a dfs over the entire tree to construct a graph
# Space complexity is O(N) and not O(V + E) since we know that each node has at most one edge

# Slightly simpler solution which involves annotating the tree nodes

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        self.dfs(root,None)
        
        q = [(target,0)]
        seen = {target}
        while q:
            if q[0][1] == k:
                return [node.val for node,d in q]
            node, d = q.pop(0)
            for nei in (node.left,node.right,node.par):
                if nei and nei not in seen:
                    q.append((nei, d + 1))
                    seen.add(nei)
        return []
        
    def dfs(self, node, parent):
        if node:
            node.par = parent
            self.dfs(node.left, node)
            self.dfs(node.right, node)

# Time complexity is O(N)

# Space complexity is O(N)