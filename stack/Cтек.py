"""
СТЕК - заготовка для практики

Практика по дисциплине "Алгоритмы и структуры данных"
Преподаватель - Добряк Павел Вадимович.
Для свободного распространения среди студентов ИРИТ-РтФ.
В Интернете в открытом доступе не публиковать!
"""
"""
Класс стек.
версия 1. Стек на одном классе - плохо подходит для персистентности
"""
"""
class stack:
    def __init__(self,val=None,prev=None):
        self.val=val
        self.prev=None
    def push(self,val):
        if self.val==None:
            self.val=val
        else:
            temp=stack()
            temp.val=self.val
            temp.prev=self.prev
            self.val=val
            self.prev=temp
    def pop(self):
        res=self.val
        if self.prev!=None:
            self.val=self.prev.val
            self.prev=self.prev.prev
        else:
            self.val=None
        return res

S=stack()

S.push(10)
S.push(20)
S.push(30)
S.push(40)
S.push(50)

print(S.pop())
print(S.pop())
print(S.pop())
print(S.pop())
print(S.pop())
print(S.pop())
"""
"""
Класс стек.
версия 2. Стек на двух классах: собственно класс стек и вложенный класс узел
"""

"""
СТЕК - заготовка для практики

Практика по дисциплине "Алгоритмы и структуры данных"
Преподаватель - Добряк Павел Вадимович.
Для свободного распространения среди студентов ИРИТ-РтФ.
В Интернете в открытом доступе не публиковать!
"""
"""
Класс стек.
версия 1. Стек на одном классе - плохо подходит для персистентности
"""
"""
class stack:
    def __init__(self,val=None,prev=None):
        self.val=val
        self.prev=None
    def push(self,val):
        if self.val==None:
            self.val=val
        else:
            temp=stack()
            temp.val=self.val
            temp.prev=self.prev
            self.val=val
            self.prev=temp
    def pop(self):
        res=self.val
        if self.prev!=None:
            self.val=self.prev.val
            self.prev=self.prev.prev
        else:
            self.val=None
        return res

S=stack()

S.push(10)
S.push(20)
S.push(30)
S.push(40)
S.push(50)

print(S.pop())
print(S.pop())
print(S.pop())
print(S.pop())
print(S.pop())
print(S.pop())
"""
"""
Класс стек.
версия 2. Стек на двух классах: собственно класс стек и вложенный класс узел
"""

class Stack:
    class Node:
        def __init__(self, val, prev=None):
            self.val = val
            self.prev = prev
            
            
    def __init__(self):
        self.versions = [None]
        
        
    def push(self, val):
        old_root = self.versions[-1]    
        new_root = self.Node(val, old_root)
        self.versions.append(new_root)
    
    
    def pop(self):
        old_root = self.versions[-1]
        
        if old_root is None:
            self.versions.append(None)
        else:
            self.versions.append(old_root.prev)
        
        
    def print_versions(self):
        for i in range(1, len(self.versions)):
            root = self.versions[i]
            elems = []
            
            while root is not None:
                elems.append(root.val)
                root = root.prev
            
            print(elems)                
        

S = Stack()

S.push(10)
S.push(15)
S.push(20)
S.pop()
S.push(25)
S.print_versions()