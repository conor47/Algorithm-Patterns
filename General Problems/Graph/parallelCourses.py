# You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.

# In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.

# Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list) 
        sources = []  
        indegree = [0] * (n + 1)
        
        for u,v in relations:
            graph[u].append(v)
            indegree[v] += 1
         
        for i in range(1,n+1):
            if indegree[i] == 0:
                sources.append(i)
        
        count = 0
        res = []
        
        while sources:
            count += 1
            for i in range(len(sources)):
                node = sources.pop(0)
                res.append(node)
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        sources.append(nei)
        if len(res) == n:
            return count 
        else:
            return -1
            return -1

# Time complexity is (V + E)

# Space complexity is O(V + E)