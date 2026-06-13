def hanoi(a, b, c, n):
    if n == 1:
        print(a, '->', c)
    else:
        hanoi(a, c, b, n-1)
        print(a, '->', c)
        hanoi(b, a, c, n-1)


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


def hyperWithoutFor(a, b, n):
    if n == 1:
        return a + b
    if b == 1:
        return a

    return hyperWithoutFor(a, hyperWithoutFor(a, b-1, n), n-1)


def hyperWithFor(a, b, n):
    if n == 1:
        return a + b
    else:
        s = a
        for _ in range(b-1):
            s = hyperWithFor(a, s, n-1)
        return s


def words(s, r):
    if r == 0:
        yield ""
    else:
        for i in s:
            for j in words(s, r-1):
                yield i+j


print("Ханойские башни:")
hanoi("A", "B", "C", 3)
print(f"Польская инверсная запись: {polish_math('1 2 + 4 /')}")
print(f"Гипероператор без цикла (рекурсия): {hyperWithoutFor(2, 3, 3)}")
print(f"Гипероператор с циклом и рекурсией: {hyperWithFor(2, 3, 3)}")
print(f"Слова произвольной длины: {list(words("ABC", 2))}")