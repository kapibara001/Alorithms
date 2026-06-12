"""
import math

class SparseTable:
    def __init__(self, arr: list):
        self.n = len(arr)
        if self.n == 0:
            self.st = []
            return

        self.k = self.n.bit_length() 

        self.st = [[0] * self.k for _ in range(self.n)]

        for i in range(self.n):
            self.st[i][0] = arr[i]

        for j in range(1, self.k):
            for i in range(self.n - (1 << j) + 1):
                self.st[i][j] = min(
                    self.st[i][j - 1], 
                    self.st[i + (1 << (j - 1))][j - 1]
                )


    def query(self, L: int, R: int):
        if L > R:
            return None
        
        length = R - L + 1
        j = length.bit_length() - 1 
        
        return min(self.st[L][j], self.st[R - (1 << j) + 1][j])


    def get_table(self):
        return self.st


arr = [1, 2, 0, 4, 5]
st = SparseTable(arr)


print("Вся таблица:")
for row in st.get_table():
    print(row)


print("\nЗапросы:")
print(f"Min [0, 4]: {st.query(0, 4)}") 
print(f"Min [0, 1]: {st.query(0, 1)}") 
print(f"Min [3, 4]: {st.query(3, 4)}") 
"""


class SparseTable:
    def __init__(self, startArr: list, func=min):
        self.n = len(startArr)
        self.func = func 
        
        if self.n == 0:
            self.result = []
            self.K = 0
            return

        self.result = [startArr[:]]  
        
        k = 1
        while (1 << k) <= self.n:
            prev_level = self.result[k - 1]
            half = 1 << (k - 1) 
            curr_level = []
            
            for i in range(self.n - (1 << k) + 1):
                curr_level.append(self.func(prev_level[i], prev_level[i + half]))
                
            self.result.append(curr_level)
            k += 1
            
        self.K = len(self.result)
        
    
    def get_st(self):
        return self.result
    
    
arr = 