# You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with m rows and n columns using all the elements from original.

# The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.

# Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        if len(original) % n != 0 or len(original) / n != m:
            return res
        
        i=0
        while i < len(original):
            res.append(original[i:i+n])
            i = i+n
            
        return res

# Time complexity O(N) where N is the length of the input array

# Space complexity is O(N) if we include the output array, otherwise its O(N) since we are taking slices of size N 

