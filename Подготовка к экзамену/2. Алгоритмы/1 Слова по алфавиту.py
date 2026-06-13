def product_analog(string, repeat):
    if repeat == 0:
        yield ""
    else:
        for i in string:
            for j in product_analog(string, repeat-1):
                yield i + j

print(list(product_analog("abc", 2)))