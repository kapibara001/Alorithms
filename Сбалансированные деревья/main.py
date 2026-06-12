from collections.abc import Iterable
from copy import copy

class Treap:
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
                self.left=Treap(L,x,y)
            if len(R)>0:
                self.right=Treap(R,x,y)
                
                
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
        M=Treap([obj],self.x,self.y)
        res=L.merge(M).merge(R)
        self.copy(res)
        
        
    def remove(self,x):
        L,R=self.split(x)
        L,M=L.split(x-10**(-5))
        res=L.merge(R)
        self.copy(res)
        
        
    def left_rotate(self):
        if self.value is None or self.right is None:
            return self

        old_root = copy(self)         
        lastright = self.right     

        old_root.right = lastright.left

        new_root = copy(lastright)
        new_root.left = old_root

        self.copy(new_root)
        return self
        
    
    def big_left_rotate(self):
        if self.right is None or self.value is None:
            return self
        
        selfroot = copy(self) # копируем текущую вершину
        # https://www.youtube.com/watch?v=4qJVFQ-LK7A понятное видео
        
            
    
    
    def right_rotate(self):
        if self.value is None or self.left is None:
            return self
        
        old_root = copy(self)
        lastleft = self.left
        
        old_root.left = lastleft.right
        
        new_root = copy(lastleft)
        new_root.right = old_root
        
        self.copy(new_root)
        return self
        
        
    def big_right_rotate(self):
        ...



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
T=Treap([A,B,C,D,E,F,G],lambda p: p.x, lambda p: p.y) 
print(T)
left_rotate_T = T.left_rotate()
print(left_rotate_T)
print(left_rotate_T.right_rotate())


def f(a, b = 1, *c):
    s = 0
    for i in c:
        s += i
        
    s *= b
    s += a
    
    return s


with open('as.txt', 'a') as test:
    for i in range(0, 5):
        test.write(str(i))
    test.write('test passed')