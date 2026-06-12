def solve_maze(maze: list[list[int]]) -> bool:
    n = len(maze)
    m = len(maze[0])

    visited = [[False] * m for _ in range(n)]
    path = []

    def dfs(x, y):
        # выход за границы или стена или уже посещали
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        if maze[x][y] == 1 or visited[x][y]:
            return False

        # добавляем клетку в путь
        path.append((x, y))
        visited[x][y] = True

        # если дошли до цели
        if x == n - 1 and y == m - 1:
            return True

        # пробуем все направления
        if (dfs(x + 1, y) or
                dfs(x - 1, y) or
                dfs(x, y + 1) or
                dfs(x, y - 1)):
            return True

        # бэктрекинг (откат)
        path.pop()
        return False

    if dfs(0, 0):
        return path
    else:
        return None


# пример
maze = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 1, 0],
    [0, 0, 0, 0]
]

print(solve_maze(maze))