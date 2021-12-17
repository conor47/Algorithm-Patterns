# You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.

# You are given an array of employees employees where:

#     employees[i].id is the ID of the ith employee.
#     employees[i].importance is the importance value of the ith employee.
#     employees[i].subordinates is a list of the IDs of the direct subordinates of the ith employee.

# Given an integer id that represents an employee's ID, return the total importance value of this employee and all their direct and indirect subordinates.

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importances = {}
        for employee in employees:
            importances[employee.id] = (employee.importance,employee.subordinates)
        
        q = []
        q.append(importances[id])
        res = 0
        
        while q:
            importance,subords = q.pop(0)
            res += importance
            
            for id in subords:
                q.append(importances[id])
        return res

# Time complexity is O(N) 

# Space complexity is O(N)