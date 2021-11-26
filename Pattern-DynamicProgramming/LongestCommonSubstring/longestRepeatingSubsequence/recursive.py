# Given a sequence, find the length of its longest repeating subsequence (LRS). A repeating subsequence will be the one that appears at least twice in the original sequence and is not overlapping (i.e. none of the corresponding characters in the repeating subsequences have the same index).

# Example 1:

# Input: “t o m o r r o w”
# Output: 2
# Explanation: The longest repeating subsequence is “or” {tomorrow}.

# Example 2:

# Input: “a a b d b c e c”
# Output: 3
# Explanation: The longest repeating subsequence is “a b c” {a a b d b c e c}.

# Example 3:

# Input: “f m f f”
# Output: 2
# Explanation: The longest repeating subsequence is “f f” {f m f f, f m f f}. Please note the second last character is shared in LRS.

def find_LRS_length(str):

    return lrs(str,0,0)

def lrs(str,idx1,idx2):
    if idx1 == len(str) or idx2 == len(str):
        return 0

    if idx1 != idx2 and str[idx1] == str[idx2]:
        return 1 + lrs(str,idx1+1,idx2+1)

    c1 = lrs(str,idx1+1,idx2)
    c2 = lrs(str,idx1,idx2+1)
    return max(c1,c2)

# Time complexity is exponential O(2^n)

# Space complexity is O(N)

def main():
  print(find_LRS_length("tomorrow"))
  print(find_LRS_length("aabdbcec"))
  print(find_LRS_length("fmff"))


main()