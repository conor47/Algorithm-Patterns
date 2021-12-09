class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        dic = {}
        self.postOrder(res,dic,'',root)
        return res
        
    def postOrder(self,res,dic,path,node):
        if node is None:
            return '#'
        
        path = str(node.val) + ',' + self.postOrder(res,dic,path,node.left) + ',' + self.postOrder(res,dic,path,node.right)
        
        dic[path] = dic.get(path,0) + 1
        if dic[path] == 2:
            res.append(node)
        return path

# Time complexity O(N)

# Space complexity is O(N)