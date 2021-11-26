# Given a string and a pattern, write a method to count the number of times the pattern appears in the string as a subsequence.

# Example 1: Input: string: “baxmx”, pattern: “ax”
# Output: 2
# Explanation: {baxmx, baxmx}.

# Example 2:

# Input: string: “tomorrow”, pattern: “tor”
# Output: 4
# Explanation: Following are the four occurences: {tomorrow, tomorrow, tomorrow, tomorrow}.

def find_SPM_count(str, pat):
    dp = [[-1 for _ in range(len(pat))] for _ in range(len(str))]
    return recursive(str,pat,0,0,dp)

def recursive(str,pat,strIdx, patIdx,dp):

    if patIdx == len(pat):
        return 1
    
    if strIdx == len(str):
        return 0

    if dp[strIdx][patIdx] == -1:


        c1 =0 
        if str[strIdx] == pat[patIdx]:
            c1 = recursive(str,pat,strIdx+1,patIdx+1,dp)
        
        c2 = recursive(str,pat,strIdx+1,patIdx,dp)

        dp[strIdx][patIdx] =  c2 + c1
    return dp[strIdx][patIdx]

def main():
  print(find_SPM_count("baxmx", "ax"))
  print(find_SPM_count("tomorrow", "tor"))


main()