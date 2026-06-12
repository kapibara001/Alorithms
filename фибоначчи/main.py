def febonachi_recursive(max_int, a=0, b=1):
    if a > max_int:
        return
    
    yield a

    yield from febonachi_recursive(max_int, b, a+b)


print(list(febonachi_recursive(22)))