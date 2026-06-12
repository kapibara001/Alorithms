def lps(s):
    n = len(s)
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > j:
            return 0
        if i == j:
            return 1

        if s[i] == s[j]:
            ans = dp(i + 1, j - 1) + 2
        else:
            ans = max(dp(i + 1, j), dp(i, j - 1))

        memo[(i, j)] = ans
        return ans

    return dp(0, n - 1)


# пример
print(lps("character"))