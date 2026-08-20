def lcs(sequence1, sequence2):
    m = len(sequence1)
    n = len(sequence2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if sequence1[i - 1] == sequence2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i = m
    j = n
    lcs_result = []

    while i > 0 and j > 0:
        if sequence1[i - 1] == sequence2[j - 1]:
            lcs_result.append(sequence1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs_result.reverse()

    return dp[m][n], lcs_result


# Input sequences
sequence1 = input("Enter the first sequence: ")
sequence2 = input("Enter the second sequence: ")

# Find LCS
length, result = lcs(sequence1, sequence2)

# Display result
print("\nLength of LCS:", length)
print("Longest Common Subsequence:", "".join(result))