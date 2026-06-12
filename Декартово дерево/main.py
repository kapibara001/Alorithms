# x - ключ по иксу, y - приоритет, по игрику

class Treap():
    def __init__(self, points:list = None, x = None, y = None):
        self.x = x
        self.y = y
        self.left = None #Treap
        self.right = None #Treap
        
        if points is not None:
            # if not points:
            #     return
            
            max_point = max(points, key=lambda p: p[1]) # по y
            
            self.x, self.y = max_point
            
            left_points = [p for p in points if p[0] < self.x]
            rigth_points = [p for p in points if p[0] > self.x]
            
            if left_points:
                self.left = Treap(left_points) #
            if rigth_points:
                self.right = Treap(rigth_points) #
        
        elif x is not None and y is not None:
            self.x = x
            self.y = y
            
            
        def merge(L, R): # L, R - Treap
            if L is None:
                return R
            if R is None:
                return L
            
            if L.y > R.y:
                newR = Treap.merge(L.right, R)
                return Treap(x=L.x, y=L.y, left=L.left, right=newR)
            else:
                newL = Treap.merge(L, R.left)
                return Treap(x=R.x, y=R.y, left=newL, right=R.right)
                
        
            
        
    
    def split(self):
        ... # применение merge
            
            
points = [(5, 20), (2, 10), (8, 15), (1, 5), (3, 7)]
treap = Treap(points)
