from collections import deque

def solve_maze(maze):
    n = len(maze)
    m = len(maze[0])

    visited = [[False]*m for _ in range(n)]
    queue = deque()

    # (координаты, путь)
    queue.append(((0, 0), [(0, 0)]))
    visited[0][0] = True

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        (x, y), path = queue.popleft()

        # если дошли до цели
        if (x, y) == (n-1, m-1):
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append(((nx, ny), path + [(nx, ny)]))

    return None  # пути нет


# пример
maze = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 1, 0],
    [0, 0, 0, 0]
]

print(solve_maze(maze))