class Heap:
    def __init__(self):
        self.heap = []


    def _sift_up(self, i):
        if i == 0:
            return

        parent = (i - 1) // 2

        if self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._sift_up(parent)


    def _sift_down(self, i):
        size = len(self.heap)
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < size and self.heap[left] > self.heap[largest]:
            largest = left
        if right < size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest == i:
            return

        self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
        self._sift_down(largest)


    def add(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)


    def pop_min(self):
        if not self.heap:
            raise IndexError("Пустая куча")

        min_index = 0
        for i in range(1, len(self.heap)):
            if self.heap[i] < self.heap[min_index]:
                min_index = i

        min_val = self.heap[min_index]

        if min_index == len(self.heap) - 1:
            self.heap.pop()
            return min_val

        self.heap[min_index], self.heap[-1] = self.heap[-1], self.heap[min_index]
        self.heap.pop()

        parent = (min_index-1) // 2 # вместо (n/2)-1
        if min_index > 0 and self.heap[min_index] > self.heap[parent]:
            self._sift_up(min_index)
        else:
            self._sift_down(min_index)

        return min_val
    

heap = Heap()

for i in [2, 3, 4, 5, 6, 7, 8, 9]:
    heap.add(i)

print(heap.pop_min())