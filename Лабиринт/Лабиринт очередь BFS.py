L = [
    [9,9,9,9,9,9,0,9,9,9],
    [9,0,9,9,9,0,0,0,0,9],
    [9,0,9,0,0,0,9,9,0,9],
    [9,0,0,0,0,9,0,0,0,9],
    [9,9,0,9,0,9,0,9,0,9],
    [9,9,0,9,9,9,0,9,0,9],
    [9,0,0,0,0,9,9,9,9,9],
    [9,0,9,9,0,9,9,0,0,9],
    [9,0,0,9,0,9,9,0,0,9],
    [9,9,0,9,9,9,9,9,9,9]
]

def show(L):
    for i in range(len(L)):
        s = ""
        for j in range(len(L[0])):
            if L[i][j] == 0:
                s += "0"
            elif L[i][j] == 9:
                s += "#"
            elif L[i][j] == 1:
                s += ">"
            elif L[i][j] == 2:
                s += "^"
            elif L[i][j] == 3:
                s += "<"
            elif L[i][j] == 4:
                s += "v"
        print(s)

def is_fork(L, x, y):
    rows = len(L)
    cols = len(L[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and L[nx][ny] == 0:
            count += 1
    
    return count > 2

def findExit(L):
    rows = len(L)
    columns = len(L[0])
    togo = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    start, finish = None, None

    for i in range(columns):
        if L[0][i] == 0:
            start = (0, i)
            break
    
    for j in range(columns):
        if L[rows - 1][j] == 0:
            finish = (rows - 1, j)
            break

    if start is None or finish is None:
        return None

    stack = [start]
    visited = set()
    visited.add(start)

    parent = {}
    forks = []

    isFound = False

    while stack:
        x, y = stack.pop()

        if is_fork(L, x, y):
            forks.append((x, y))

        if (x, y) == finish:
            isFound = True
            break

        for dx, dy in togo:
            nx, ny = x + dx, y + dy

            if 0 <= ny <= rows and 0 <= nx <= columns:
                if L[nx][ny] == 0 and L[nx][ny] not in visited:
                    visited.add((nx, ny))
                    parent[x, y] = (x, y)
                    stack.append((nx, ny))

        if not isFound:
            print("Выход не найден")
            return None

    path = []
    cur = finish

    while cur != start:
        path.append(cur)
        cur = parent[cur]
    
    path.append(start)
    path.reverse()

        for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]

        if x2 == x1 and y2 == y1 + 1:
            L[x1][y1] = 1  
        elif x2 == x1 - 1 and y2 == y1:
            L[x1][y1] = 2  
        elif x2 == x1 and y2 == y1 - 1:
            L[x1][y1] = 3  
        elif x2 == x1 + 1 and y2 == y1:
            L[x1][y1] = 4   

    return forks, path