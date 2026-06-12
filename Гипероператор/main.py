def sum(a, b):
    return a+b


def mult(num, times):
    res = num
    for i in range(times-1):
        res = sum(res, num)

    return res


def power(num, sup):
    res = num
    for i in range(sup-1):
        res = mult(res, num)

    return res


def tetra(num, times):
    res = num
    for i in range(times):
        res = power(res, num)

    return res


def penta(num, times):
    res = num
    for i in range(times):
        res = tetra(res, num)

    return res
    

def hyper(a, b, n):
    if n == 1:
        return a + b
    else:  
        s = a 
        for i in range(b-1):
            s = hyper(a, s, n-1)
        return s

print(hyper(1, 2, 1))