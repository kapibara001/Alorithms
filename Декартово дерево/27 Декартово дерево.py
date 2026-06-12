"""
ДЕКАРТОВО ДЕРЕВО

Практика по дисциплине "Алгоритмы и структуры данных"
Преподаватель - Добряк Павел Вадимович.
Для свободного распространения среди студентов ИРИТ-РтФ.
В Интернете в открытом доступе не публиковать!
"""
"""
Инициализатор из итерируемой коллекции
"""
"""
from collections.abc import Iterable

class treap:
    def __init__(self, arg, x=lambda arg:arg[0], y=lambda arg:arg[1]):
        self.value=None
        self.left=None
        self.right=None
        self.x=x
        self.y=y
        if not isinstance(arg,Iterable):
            self.value=arg
        else:
            self.value=max(arg,key=self.y)
            L=[]
            R=[]
            for a in arg:
                if a!=self.value:
                    if self.x(a)<=self.x(self.value):
                        L.append(a)
                    else:
                        R.append(a)
            if len(L)>0:
                self.left=treap(L,x,y)
            if len(R)>0:
                self.right=treap(R,x,y)
    def __str__(self):
        s=""
        if self.value!=None:
            s=s+repr(self.value)
            if self.left!=None or self.right!=None:
                s=s+"["
                if self.left!=None:
                    s=s+str(self.left)
                s=s+","
                if self.right!=None:
                    s=s+str(self.right)
                s=s+"]"
        return s

class point:
    def __init__(self,x=0,y=0,name=""):
        self.x=x
        self.y=y
        self.name=name
    def __str__(self):
        return f"{self.name}({self.x},{self.y})"
    def __repr__(self):
        return f"{self.name}"

A=point(5,10,"A")
B=point(2,7,"B")
C=point(7,8,"C")
D=point(1,2,"D")
E=point(6,5,"E")
F=point(4,4,"F")
G=point(8,3,"G")
T=treap([A,B,C,D,E,F,G],lambda p: p.x, lambda p: p.y) 
print(T)
"""
"""
Объединение непересекающихся по ключам x деревьев
"""
"""
from collections.abc import Iterable
from copy import copy

class treap:
    def __init__(self, arg, x=lambda arg:arg[0], y=lambda arg:arg[1]):
        self.value=None
        self.left=None
        self.right=None
        self.x=x
        self.y=y
        if not isinstance(arg,Iterable):
            self.value=arg
        else:
            self.value=max(arg,key=self.y)
            L=[]
            R=[]
            for a in arg:
                if a!=self.value:
                    if self.x(a)<=self.x(self.value):
                        L.append(a)
                    else:
                        R.append(a)
            if len(L)>0:
                self.left=treap(L,x,y)
            if len(R)>0:
                self.right=treap(R,x,y)
    def __str__(self):
        s=""
        if self.value!=None:
            s=s+repr(self.value)
            if self.left!=None or self.right!=None:
                s=s+"["
                if self.left!=None:
                    s=s+str(self.left)
                s=s+","
                if self.right!=None:
                    s=s+str(self.right)
                s=s+"]"
        return s
    def merge(self,other):
        if other==None:
            return self
        if self.y(self.value)>=other.y(other.value):
            root=copy(self)
            if self.x(self.value)<=other.x(other.value):
                root.right=other.merge(self.right)
            else:
                root.left=other.merge(self.left)
        else:
            root=copy(other)
            if other.x(other.value)<=self.x(self.value):
                root.right=self.merge(other.right)
            else:
                root.left=self.merge(other.left)
        return root

class point:
    def __init__(self,x=0,y=0,name=""):
        self.x=x
        self.y=y
        self.name=name
    def __str__(self):
        return f"{self.name}({self.x},{self.y})"
    def __repr__(self):
        return f"{self.name}"

A=point(5,10,"A")
B=point(2,7,"B")
C=point(7,8,"C")
D=point(1,2,"D")
E=point(6,5,"E")
F=point(4,4,"F")
G=point(8,3,"G")
T=treap([A,B,C,D,E,F,G],lambda p: p.x, lambda p: p.y) 
print(T)
H=point(11,9,"H")
I=point(10,6,"I")
J=point(12,1,"J")
U=treap([H,I,J],lambda p: p.x, lambda p: p.y) 
print(U)
print(T.merge(U))
print(U.merge(T))
"""
"""
Напишем метод разбиения по значению x на два дерева
"""
"""
from collections.abc import Iterable
from copy import copy

class treap:
    def __init__(self, arg, x=lambda arg:arg[0], y=lambda arg:arg[1]):
        self.value=None
        self.left=None
        self.right=None
        self.x=x
        self.y=y
        if not isinstance(arg,Iterable):
            self.value=arg
        else:
            self.value=max(arg,key=self.y)
            L=[]
            R=[]
            for a in arg:
                if a!=self.value:
                    if self.x(a)<=self.x(self.value):
                        L.append(a)
                    else:
                        R.append(a)
            if len(L)>0:
                self.left=treap(L,x,y)
            if len(R)>0:
                self.right=treap(R,x,y)
    def __str__(self):
        s=""
        if self.value!=None:
            s=s+repr(self.value)
            if self.left!=None or self.right!=None:
                s=s+"["
                if self.left!=None:
                    s=s+str(self.left)
                s=s+","
                if self.right!=None:
                    s=s+str(self.right)
                s=s+"]"
        return s
    def merge(self,other):
        if other==None:
            return self
        if self.y(self.value)>=other.y(other.value):
            root=copy(self)
            if self.x(self.value)<=other.x(other.value):
                root.right=other.merge(self.right)
            else:
                root.left=other.merge(self.left)
        else:
            root=copy(other)
            if other.x(other.value)<=self.x(self.value):
                root.right=self.merge(other.right)
            else:
                root.left=self.merge(other.left)
        return root
    def split(self,x):
        if self.x(self.value)<=x:
            L=copy(self)
            if self.right!=None:
                M,R=L.right.split(x)
            else:
                R=None
                M=None
            L.right=M
            return L,R
        else:
            R=copy(self)
            if self.left!=None:
                L,M=R.left.split(x)
            else:
                L=None
                M=None
            R.left=M
            return L,R

class point:
    def __init__(self,x=0,y=0,name=""):
        self.x=x
        self.y=y
        self.name=name
    def __str__(self):
        return f"{self.name}({self.x},{self.y})"
    def __repr__(self):
        return f"{self.name}"

A=point(5,10,"A")
B=point(2,7,"B")
C=point(7,8,"C")
D=point(1,2,"D")
E=point(6,5,"E")
F=point(4,4,"F")
G=point(8,3,"G")
T=treap([A,B,C,D,E,F,G],lambda p: p.x, lambda p: p.y) 
H=point(11,9,"H")
I=point(10,6,"I")
J=point(12,1,"J")
U=treap([H,I,J],lambda p: p.x, lambda p: p.y)  
V=T.merge(U)
print(V)
L,R=V.split(9)
print(L)
print(R)
"""
"""
Добавление элемента
"""
"""
from collections.abc import Iterable
from copy import copy

class treap:
    def __init__(self, arg, x=lambda arg:arg[0], y=lambda arg:arg[1]):
        self.value=None
        self.left=None
        self.right=None
        self.x=x
        self.y=y
        if not isinstance(arg,Iterable):
            self.value=arg
        else:
            self.value=max(arg,key=self.y)
            L=[]
            R=[]
            for a in arg:
                if a!=self.value:
                    if self.x(a)<=self.x(self.value):
                        L.append(a)
                    else:
                        R.append(a)
            if len(L)>0:
                self.left=treap(L,x,y)
            if len(R)>0:
                self.right=treap(R,x,y)
    def __str__(self):
        s=""
        if self.value!=None:
            s=s+repr(self.value)
            if self.left!=None or self.right!=None:
                s=s+"["
                if self.left!=None:
                    s=s+str(self.left)
                s=s+","
                if self.right!=None:
                    s=s+str(self.right)
                s=s+"]"
        return s
    def merge(self,other):
        if other==None:
            return self
        if self.y(self.value)>=other.y(other.value):
            root=copy(self)
            if self.x(self.value)<=other.x(other.value):
                root.right=other.merge(self.right)
            else:
                root.left=other.merge(self.left)
        else:
            root=copy(other)
            if other.x(other.value)<=self.x(self.value):
                root.right=self.merge(other.right)
            else:
                root.left=self.merge(other.left)
        return root
    def split(self,x):
        if self.x(self.value)<=x:
            L=copy(self)
            if self.right!=None:
                M,R=L.right.split(x)
            else:
                R=None
                M=None
            L.right=M
            return L,R
        else:
            R=copy(self)
            if self.left!=None:
                L,M=R.left.split(x)
            else:
                L=None
                M=None
            R.left=M
            return L,R
    def copy(self,other):
        self.value=other.value
        self.left=other.left
        self.right=other.right
        self.x=other.x
        self.y=other.y
    def add(self,obj):
        L,R=self.split(self.x(obj))
        M=treap([obj],self.x,self.y)
        res=L.merge(M).merge(R)
        self.copy(res)

class point:
    def __init__(self,x=0,y=0,name=""):
        self.x=x
        self.y=y
        self.name=name
    def __str__(self):
        return f"{self.name}({self.x},{self.y})"
    def __repr__(self):
        return f"{self.name}"

A=point(5,10,"A")
B=point(2,7,"B")
C=point(7,8,"C")
D=point(1,2,"D")
E=point(6,5,"E")
F=point(4,4,"F")
G=point(8,3,"G")
T=treap([A,B,C,D,E,F,G],lambda p: p.x, lambda p: p.y) 
print(T)
K=point(3,6,"K")
T.add(K)
print(T)
"""
"""
Удаление элемента
"""

from collections.abc import Iterable
from copy import copy


class treap:
    def __init__(self, arg, x=lambda arg:arg[0], y=lambda arg:arg[1]):
        self.value=None
        self.left=None
        self.right=None
        self.x=x
        self.y=y
        
        if not isinstance(arg,Iterable):
            self.value=arg
        else:
            self.value=max(arg,key=self.y)
            L=[]
            R=[]
            for a in arg:
                if a!=self.value:
                    if self.x(a)<=self.x(self.value):
                        L.append(a)
                    else:
                        R.append(a)
            if len(L)>0:
                self.left=treap(L,x,y)
            if len(R)>0:
                self.right=treap(R,x,y)
                
                
    def __str__(self):
        s=""
        if self.value!=None:
            s=s+repr(self.value)
            if self.left!=None or self.right!=None:
                s=s+"["
                if self.left!=None:
                    s=s+str(self.left)
                s=s+","
                if self.right!=None:
                    s=s+str(self.right)
                s=s+"]"
        return s
    
    
    def merge(self,other):
        if other==None:
            return self
        if self.y(self.value)>=other.y(other.value):
            root=copy(self)
            if self.x(self.value)<=other.x(other.value):
                root.right=other.merge(self.right)
            else:
                root.left=other.merge(self.left)
        else:
            root=copy(other)
            if other.x(other.value)<=self.x(self.value):
                root.right=self.merge(other.right)
            else:
                root.left=self.merge(other.left)
        return root
    
    
    def split(self,x):
        if self.x(self.value)<=x:
            L=copy(self)
            
            if self.right!=None:
                M,R=L.right.split(x)
            else:
                R=None
                M=None
                
            L.right=M
            
            return L,R
        else:
            R=copy(self)
            if self.left!=None:
                L,M=R.left.split(x)
            else:
                L=None
                M=None
            R.left=M
            return L,R
    def copy(self,other):
        self.value=other.value
        self.left=other.left
        self.right=other.right
        self.x=other.x
        self.y=other.y
    def add(self,obj):
        L,R=self.split(self.x(obj))
        M=treap([obj],self.x,self.y)
        res=L.merge(M).merge(R)
        self.copy(res)
    def remove(self,x):
        L,R=self.split(x)
        L,M=L.split(x-10**(-5))
        res=L.merge(R)
        self.copy(res)
        
        
    

class point:
    def __init__(self,x=0,y=0,name=""):
        self.x=x
        self.y=y
        self.name=name
    def __str__(self):
        return f"{self.name}({self.x},{self.y})"
    def __repr__(self):
        return f"{self.name}"


A=point(5,10,"A")
B=point(2,7,"B")
C=point(7,8,"C")
D=point(1,2,"D")
E=point(6,5,"E")
F=point(4,4,"F")
G=point(8,3,"G")
T=treap([A,B,C,D,E,F,G],lambda p: p.x, lambda p: p.y) 
print(T)
T.remove(2)
print(T)

