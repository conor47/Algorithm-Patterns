# You have n processes forming a rooted tree structure. You are given two integer arrays pid and ppid, where pid[i] is the ID of the ith process and ppid[i] is the ID of the ith process's parent process.

# Each process has only one parent process but may have multiple children processes. Only one process has ppid[i] = 0, which means this process has no parent process (the root of the tree).

# When a process is killed, all of its children processes will also be killed

# Given an integer kill representing the ID of a process you want to kill, return a list of the IDs of the processes that will be killed. You may return the answer in any order.

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        parentChild = defaultdict(list) 
        for i in range(len(ppid)):
            parentChild[ppid[i]].append(pid[i])
        
        res = []
        killed = set()
        q = [kill]
        while q:
            id = q.pop()
            killed.add(id)
            res.append(id)
            for child in parentChild[id]:
                if child not in killed:
                    q.append(child)
        return res

# Time complexity is O(N)

# Space complexity is O(N)