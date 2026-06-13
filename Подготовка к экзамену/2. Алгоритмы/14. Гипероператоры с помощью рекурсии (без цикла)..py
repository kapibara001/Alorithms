def hyper(n, a, b):
    if n == 1:
        return a + b

    if b == 1:
        return a

    return hyper(n - 1, a, hyper(n, a, b - 1))

print(hyper(4, 3, 3))