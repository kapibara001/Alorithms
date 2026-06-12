def is_prime(a: list):
    for i in a[:]:
        if i == 1:
            continue

        num = i
        while num <= max(a):
            num += i
            try:
                a.remove(num)
            except ValueError:
                continue

    return a


array = [i for i in range(1, 31)]
print(is_prime(array))
# is_prime(array)