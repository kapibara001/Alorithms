def binary_search(arr, t):
    """
    Бинарный поиск. Решается просто перемещением правой или левой границы. Еще важно
    middle = (left + right) // 2
    """
    left = 0
    right = len(arr) - 1
    while right >= left:
        middle = (left + right) // 2
        if arr[middle] == t:
            return middle
        elif arr[middle] < t:
            left = middle
        else:
            right = middle

arr = [2, 9, 13, 15, 88, 100, 110]
target = 15
print(f"Искомный элемент {target} в массиве {arr} имеет индекс {binary_search(arr, target)}")