def binary_search(arr, t):
    left = 0
    right = len(arr) - 1
    while left < right:
        middle = (left + right) // 2
        if arr[middle] == t:
            return middle
        else:
            if t > arr[middle]:
                left = middle
            if t < arr[middle]:
                right = middle
    return -1
print(f"Бинарный поиск 6 в [1, 2, 3, 4, 5, 6, 7]: {binary_search([1, 2, 3, 4, 5, 6, 7], 6)}")


phi = (1+5**0.5)/2
def golden_search(arr, t, L=0, R=None):
    if R is None:
        R = len(arr) -1

    CR = L + int((R-L)/phi)
    CL = R - int((R-L)/phi)

    if t == arr[CL]:
        return CL
    if t == arr[CR]:
        return CR

    if t > arr[CL]:
        return golden_search(arr, t, CL+1, R)
    elif t < arr[CR]:
        return golden_search(arr, t, L, CR-1)
    else:
        return golden_search(arr, t, CL+1, CR-1)
print(f"Поиск золотым сечением target=3, arr=[1, 2, 3, 4, 5]: {golden_search([1, 2, 3, 4, 5], 3)}")


def checking_bracket(s):
    bracket = {
        '}': '{',
        ')': '(',
        ']': '[',
    }
    openings = set(bracket.values())
    stack = []

    for i in s:
        if i in openings:
            stack.append(i)
        else:
            if stack.pop() != bracket[i]:
                return False

    return not stack
print(f"Проверка строки '[][)', '[][]': {checking_bracket('[][)')}, {checking_bracket('[][]')}")


def hanoi(a, b, c, n):
    if n == 1:
        print(a, '->', c)
    else:
        hanoi(a, c, b, n-1)
        print(a, '->', c)
        hanoi(b, a, c, n-1)
print("Ханойские башни:")
hanoi("A", "B", "C", 3)


def polish_math(s):
    s = s.split(" ")
    stack = []

    for i in s:
        try:
            stack.append(float(i))
        except ValueError:
            second = stack.pop()
            first = stack.pop()
            if i in ['+', '-', '*', '/']:
                if i == '+':
                    stack.append(first + second)
                elif i == '-':
                    stack.append(first - second)
                elif i == '/':
                    stack.append(first / second)
                elif i == '*':
                    stack.append(first * second)

    if len(stack) == 1:
        return stack[0]
print(f"Польская инверсная запись: {polish_math('1 2 + 4 /')}")


def hyperWithoutFor(a, b, n):
    if n == 1:
        return a + b
    if b == 1:
        return a

    return hyperWithoutFor(a, hyperWithoutFor(a, b-1, n), n-1)
print(f"Гипероператор без цикла (рекурсия): {hyperWithoutFor(2, 3, 3)}")


def hyperWithFor(a, b, n):
    if n == 1:
        return a + b
    else:
        s = a
        for _ in range(b-1):
            s = hyperWithFor(a, s, n-1)
        return s
print(f"Гипероператор с циклом и рекурсией: {hyperWithFor(2, 3, 3)}")


def words(s, r):
    if r == 0:
        yield ""
    else:
        for i in s:
            for j in words(s, r-1):
                yield i+j
print(f"Слова произвольной длины: {list(words("ABC", 2))}")


def quick_sort_razdeleniem(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    center = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort_razdeleniem(left) + center + quick_sort_razdeleniem(right)
print(f"Сортировка разделением (быстрая сортировка) [1, 8, 3, 6, 2, 6, 8, 9, 12, 15, 44, 11]: "
      f"{quick_sort_razdeleniem([1, 8, 3, 6, 2, 6, 8, 9, 12, 15, 44, 11])}")


def quick_sort_sliyaniem(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = quick_sort_sliyaniem(arr[:mid])
    right = quick_sort_sliyaniem(arr[mid:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
print(f"Сортировка [1, 9, 2, 3, 4, 8, 7, 5, 6] разделением: {quick_sort_sliyaniem([1, 9, 2, 3, 4, 8, 7, 5, 6])}")


def palindrome(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1]
print(f"Палиндром без кэширования 'character': {palindrome('character')}")


def palindromeCache(s):
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > j:
            return ""
        elif i == j:
            return s[j]

        if s[i] == s[j]:
            return s[i] + dp(i+1, j-1) + s[j]
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
print(f"Палиндром с кэшированием для 'character': {palindromeCache('character')}")


def max_zero_square(matrix):
    n = len(matrix)
    m = len(matrix[0])
    dp = [[0]*m for _ in range(n)]

    max_size = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1],
                    )
                max_size = max(max_size, dp[i][j])

    return max_size
print("Поиск максимального квадрата из нулей в матрице:", max_zero_square([
    [0, 0, 1],
    [0, 0, 1],
    [1, 0, 1]
]))


def max_zero_square_cache(matrix):
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
                dp(i+1, j),
                dp(i, j+1),
                dp(i+1, j+1),
            )

        return memo[(i, j)]

    max_size = 0
    for i in range(n):
        for j in range(m):
            max_size = max(max_size, dp(i, j))

    return max_size
print("Поиск максимального квадрата из нулей в матрице с кэшированием:",
      max_zero_square_cache([
        [0, 0, 1],
        [1, 0, 1],
        [1, 0, 1]
]))