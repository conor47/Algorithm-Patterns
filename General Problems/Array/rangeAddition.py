# You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].

# You have an array arr of length length with all zeros, and you have some operation to apply on arr. In the ith operation, you should increment all the elements arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.

# Return arr after applying all the updates.

# class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0]  * length
        updates.sort()
        acc = 0
        i = 0 
        while i < len(updates):
            if i < len(updates) - 1 and updates[i] == updates[i+1]:
                acc += updates[i][2] 
                i += 1
                continue
            elif acc:
                for j in range(updates[i][0],updates[i][1]+1):
                    arr[j] += acc
                acc = 0
                if i == len(updates) - 1:
                    for j in range(updates[i][0],updates[i][1]+1):
                        arr[j] += updates[i][2]
                    
                i += 1
                continue
            else:
                for j in range(updates[i][0],updates[i][1]+1):
                    arr[j] += updates[i][2]
                i += 1
        return arr

# Time complexity is O(N * M) where N is the length of the array and M is the number of updates

# Space complexity is (N)