def solve_maze(maze):
    n = len(maze)
    m = len(maze[0])

    visited = [[False]*m for _ in range(n)]

    # стек: (координаты, текущий путь)
    stack = [((0, 0), [(0, 0)])]
    visited[0][0] = True

    # направления: вниз, вверх, вправо, влево
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while stack:
        (x, y), path = stack.pop()

        # дошли до цели
        if (x, y) == (n-1, m-1):
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append(((nx, ny), path + [(nx, ny)]))

    return None  # пути нет


# пример
maze = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 1, 0],
    [0, 0, 0, 0]
]

print(solve_maze(maze))