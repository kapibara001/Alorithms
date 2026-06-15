def lps_string(s):
    """
    Считаем сам палиндром (восстанавливая его)
    """

    memo = {} # Заготовка для кэширования(хранения результата).
    # Рекурсия считала бы одно и то же много раз

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > j:
            return ""
        if i == j:
            return s[i]

        if s[i] == s[j]:
            res = s[i] + dp(i+1, j-1) + s[j]
        else:
            left = dp(i+1, j)
            right = dp(i, j-1)

            if len(left) > len(right):
                res = left
            else:
                res = right

        memo[(i, j)] = res
        return res

    return dp(0, len(s)-1)


print(lps_string("character"))