# Префиксная сумма: [1, 2, 3, 4, 5] --> [1, 3, 6, 10, 15]
# Но если поменять один элемент, придется пересчитывать все -> не круто
# Поэтому строим полное бинарное дерево (дерево отрезков)
 
""" примерный план
1. Создание массива длиной len(arr)*2
2. Дополнить массив до 2**n элементов нулями 
3. Первый элемент пустой (0)
4. Родитель: i//2, левый ребенок: i*2, правый ребенок i*2+1
5. Вернуть получившийся массив
6. Создать функцию суммы от и до
    6.1 
"""

class SegmentTree():
    def __init__(self, start_arr):
        self.start_arr = start_arr
        self.n = 1
        
        while self.n < len(start_arr): 
            self.n *= 2
            
        self.tree = [0]*(2*self.n)
        
        for i in range(len(start_arr)):
            self.tree[i+self.n] = self.start_arr[i]
            
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[i*2] + self.tree[i*2+1]
            
    
    def get_tree(self):
        return self.tree[1:]


    def sum(self, left, right):
        if not self.tree:
            raise ValueError('Дерево не инициализированно')
        
        # Если left - правый ребенок, добавить его и сдвигать left вправо
        # Если right - правый ребенок, сдвигаем right влево и добавляем
        # Поднимаемся на уровень выше
        
        result = 0
        left += self.n
        right += self.n
        
        while left < right:
            if left % 2 != 0:
                result += self.tree[left]
                left += 1
                
            if right % 2 != 0:
                result += self.tree(right)
                right += 1
                
            left //= 2
            right //= 2
            
        return result
        
        
st1 = SegmentTree([1, 2, 3, 4])
st2 = SegmentTree([1, 2, 3, 4, 5])

print(st1.get_tree())        
print(st1.sum(1, 3))    # [2, 3]
print(st2.get_tree())
print(st2.sum(1, 4))    # [2, 3, 4]