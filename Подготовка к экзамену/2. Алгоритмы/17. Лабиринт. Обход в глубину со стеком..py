def get_maze_path_stack(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    path = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    stack = [(start[0], start[1], 0)]  # x, y, индекс направления

    while stack:
        x, y, direction_index = stack[-1]

        # если первый раз пришли в клетку
        if (x, y) not in visited:
            visited.add((x, y))
            path.append((x, y))

            if (x, y) == end:
                return path

        # если все направления просмотрели — откат
        if direction_index == 4:
            stack.pop()
            path.pop()
            continue

        # иначе пробуем следующее направление
        dx, dy = directions[direction_index]
        stack[-1] = (x, y, direction_index + 1)

        nx, ny = x + dx, y + dy

        if (0 <= nx < cols and
            0 <= ny < rows and
            maze[ny][nx] == 0 and
            (nx, ny) not in visited):

            stack.append((nx, ny, 0))

    return []


grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (0, 4)
result_path = get_maze_path_stack(grid, start, end)
print(result_path)