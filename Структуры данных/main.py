class inTree:
    class Node:
        def __init__(self, value, parent=None):
            self.value = value
            self.left = None
            self.right = None
            self.parent = parent


    def __init__(self):
        self.root = None


    def _add(self, v, value: int):
        if value < v.value:
            if v.left is None:
                v.left = self.Node(value, v)
                return
            
            self._add(v.left, value)
        else:
            if v.right is None:
                v.right = self.Node(value, v)
                return
            
            self._add(v.right, value)


    def add(self, value: int):
        if self.root is None:
            self.root = self.Node(value)
            return
        
        self._add(self.root, value)


    def flat(self):
        ...


    # def fromArray(self, a, l, r):
    #     if l >= r:
    #         return None

    #     if l + 1 == r:
    #         return self.Node(a[l], None)

    #     n = (l + r) // 2
    #     t = self.Node(a[n], None)
    #     t.left = self.fromArray(a, l, n)
    #     t.right = self.fromArray(a, n + 1, r)

    #     if t.left is not None:
    #         t.left.parent = t

    #     if t.right is not None:
    #         t.right.parent = t

    #     return t


    # def _fromArray(self, a):
    #     res = inTree()
    #     res.root = self.fromArray(a, 0, len(a))
    #     return res
    

# arr = [1, 3, 5, 10, 15, 20]
# loader = inTree()
# loader.add(6)
# tree = loader._fromArray(arr)

# print(tree.root.value)