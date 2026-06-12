def max_zero_square(matrix):
    if not matrix:
        return 0

    n = len(matrix)
    m = len(matrix[0])
    memo = {}

    def dp(i, j):
        if i >= n or j >= m:
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        if matrix[i][j] == 1:
            memo[(i, j)] = 0
        else:
            memo[(i, j)] = 1 + min(
                dp(i + 1, j),
                dp(i, j + 1),
                dp(i + 1, j + 1)
            )

        return memo[(i, j)]

    max_side = 0
    for i in range(n):
        for j in range(m):
            max_side = max(max_side, dp(i, j))

    return max_side


# пример
matrix = [
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 0]
]

print(max_zero_square(matrix))