from collections import deque


def get_maze_path_bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    # Очередь хранит кортежи: (текущая_клетка, путь_до_нее)
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        (r, c), path = queue.popleft()

        if (r, c) == end:
            return path

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))

    return []


grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start_point = (0, 0)
end_point = (4, 4)

result_path = get_maze_path_bfs(grid, start_point, end_point)
print(result_path)