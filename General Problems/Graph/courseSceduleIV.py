# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

#     For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.

# Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

# You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

# Return a boolean array answer, where answer[j] is the answer to the jth query.

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)
        
        res = []
        for i,j in queries:
            res.append(self.dfs(i,graph,j,set()))
        return res
    
    def dfs(self,node,graph,target,visited):
        if node == target:
            return True
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                if self.dfs(nei,graph,target,visited):
                    return True
        return False

# Time complexity is 