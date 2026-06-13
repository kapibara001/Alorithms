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