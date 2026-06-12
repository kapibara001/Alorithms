import math

def num_to_sup(num, n, start_n):
    if n != 2:
        if n % 2 == 0:
            num_to_sup(num, n//2, start_n)
        elif n % 2 != 0:
            num_to_sup(num, int(math.floor(num/2)), start_n)
    elif n in [1, 2]:
        ...


num_to_sup(15, 3, 3)