# Вся суть стека в том, что эл-т последним пришел, первым ушел (забитое метро)
"""
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, *args):
        for i in args:
            self.items.append(i)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Стек пуск. Неоткуда брать элементы.")

    def clear(self):
        if self.is_empty():
            print("Стек уже пуст.")
        else:
            self.items = []
    
stack = Stack()     
stack.push(15, 22, 55)
print(stack.items)
print(stack.pop(), stack.items)
stack.clear()
print(stack.items)
stack.push(24)
print(stack.items)
"""

# randStr = "{[{((({{)(})))}}}]}"
# # randStr = "[({})]"

# def isValidString(string: str):
#     res = []
#     rights = {'}': '{', 
#               ']': '[',
#               ')': '(',}

#     for i in string: 
#         if i in rights.values():
#             res.append(i)
#         elif i in rights.keys():
#             if not res or res.pop() != rights[i]:
#                 return False
#         else:
#             continue

#     return not res

# print(isValidString(randStr))

mylist = [[]]
mylist[0] = [1]
mylist.append([*mylist[0], 2]) # Если длина массива mylist = 1, то не ставим *
mylist.append([*mylist[1], 3]) # иначе ставим
mylist.append([*mylist[2], 4])
print(mylist)