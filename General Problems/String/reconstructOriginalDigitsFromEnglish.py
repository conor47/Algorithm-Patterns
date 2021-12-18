# Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.

 

# Example 1:

# Input: s = "owoztneoer"
# Output: "012"

# Example 2:

# Input: s = "fviefuro"
# Output: "45"

 

# Constraints:

#     1 <= s.length <= 105
#     s[i] is one of the characters ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].
#     s is guaranteed to be valid.

class Solution:
    def originalDigits(self, s: str) -> str:
        count = collections.Counter(s)
        
        out = {}
        
        out['0'] = count['z']
        out['2'] = count ['w']
        out['4'] = count ['u']
        out['6'] = count ['x']
        out['8'] = count ['g']
        out['3'] = count['h'] - out['8']
        out['5'] = count['f'] - out['4']
        out['7'] = count['s'] - out['6']
        out['9'] = count['i'] - out['5'] - out['8'] - out['6']
        out['1'] = count['n'] - out['7'] - 2 * out['9']
        
        res = [key * out[key] for key in sorted(out.keys())]
        return ''.join(res)

# Time complexity is O(N)

# Space complextiy is O(1)