class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(defaultdict)
        
        def backtrack(current, target, acc,visited):
            visited.add(current)
            
            ret = -1.0
            neighbours = graph[current]
            
            if target in neighbours:
                ret = acc * neighbours[target]
            else:
                for neighbour,value in neighbours.items():
                    if neighbour in visited:
                        continue
                    ret = backtrack(neighbour,target,acc * value,visited)
                    if ret != -1.0:
                        break
            visited.remove(current)
            return ret
        
        for (dividend,divisor),value in zip(equations,values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value
        
        results = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                ret = -1.0
                
            elif divisor == dividend:
                ret = 1.0
                
            else:
                visited = set()
                ret = backtrack(dividend,divisor,1,visited)
            results.append(ret)
            
        return results

# Time complexity is O(M * N). We iterate accross the equations to build the graph. This takes O(N) time. For each query we must traverse the graph
# which in the worst case may take O(N) time thus processign the queries takes O(M * N) time. In total the time complexity is O(N) + O(M * N)
# which is O(M * N)

# Space complexity O(N). In the worst case where there is no overlap among the equations we would have N edges and 2N nodes. Space complexity
# is O(N + 2N) which is O(N)

# Alternative approach using Union find 

