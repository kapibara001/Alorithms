def hyper(n, a, b):
    if n == 0:
        return b + 1

    if n == 1:
        return a + b

    if n == 2:
        return a * b

    if n == 3:
        return a ** b

    if b == 0:
        return 1

    return hyper(n - 1, a, hyper(n, a, b - 1))


# примеры
print(hyper(1, 3, 4))  # 7
print(hyper(2, 3, 4))  # 12
print(hyper(3, 3, 4))  # 81
print(hyper(4, 2, 3))  # 16 (2^(2^2))