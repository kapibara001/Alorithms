
def hyper(a,b,n):
    """
    a — основание
    b — сколько раз применяем операцию
    n — уровень операции
    """
    if n==1:
        return a+b
    else:
        s=a
        for i in range(b-1):
            s=hyper(a,s,n-1)
        return s

print(hyper(2,4,4))
print(hyper(2,3,5))
print(hyper(2,2,6))
print(hyper(3,4,3))
print(hyper(3,5,3))
print(hyper(3,2,4))