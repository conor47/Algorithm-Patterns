def find_SPM_count(s,pat):
    strLen,patLen = len(s),len(pat)

    if patLen == 0:
        return 1

    if strLen == 0 or patLen > strLen:
        return 0

    dp = [[0 for _ in range(patLen + 1)] for _ in range(strLen + 1)]

    for i in range(strLen + 1):
        dp[i][0] = 1

    for i in range(1,strLen + 1):
        for j in range(1,patLen + 1):
            if s[i-1] == pat[j-1]:
                dp[i][j] = dp[i-1][j-1]
            dp[i][j] += dp[i-1][j]

    return dp[strLen][patLen]


def main():
  print(find_SPM_count("baxmx", "ax"))
  print(find_SPM_count("tomorrow", "tor"))


main()