def get_maze_path_stack(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    stack = [(start, [start])]
    visited = set()

    while stack:
        (r, c), path = stack.pop()

        if (r, c) == end:
            return path

        if (r, c) not in visited:
            visited.add((r, c))

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                    if (nr, nc) not in visited:
                        stack.append(((nr, nc), path + [(nr, nc)]))

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

result_path = get_maze_path_stack(grid, start_point, end_point)
print(result_path)