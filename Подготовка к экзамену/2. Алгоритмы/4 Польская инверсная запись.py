def polish_read(s: str):
    """
    Функция для польской инверсной записи
    """
    mystring = s.split(' ')
    stack = []
    
    if not mystring:
        return
    
    for i in mystring:
        try:
            symbol = float(i)
            stack.append(symbol)
        except ValueError:
            el2 = stack.pop()
            el1 = stack.pop()
            
            if i == '+':
                stack.append(el1 + el2)
            elif i == '-':
                stack.append(el1 - el2)
            elif i == '*':
                stack.append(el1 * el2)
            elif i == '/':
                stack.append(el1 / el2)
        
    return stack


print(polish_read('1 2 +'))
print(polish_read('1 5 / 4 *'))