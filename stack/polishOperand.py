class Word:
    def __init__(self):
        ...
    
    
polOper = [2, 3, '/', 5,  5, '+', '*']


def polishOperand(s: list):
    stack = []
    operands = ['+', '-', '*', '/']
    for i in s:
        if type(i) is int:
            stack.append(i)
        elif i in operands:
            first = stack.pop()
            second = stack.pop()

            if i == '+':
                result = first + second
            elif i == '-':
                result = first - second
            elif i == '*':
                result = first * second
            elif i == "/":
                result = first / second
            else:
                return False
            
            stack.append(result)

    return stack


print(polishOperand(polOper))

