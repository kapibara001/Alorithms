def get_maze_path(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    path = []

    def dfs(x, y):
        if x < 0 or x >= cols or y < 0 or y >= rows:
            return False
        if maze[y][x] == 1 or (x, y) in visited:
            return False

        visited.add((x, y))
        path.append((x, y))

        if (x, y) == end:
            return True

        if dfs(x - 1, y) or dfs(x + 1, y) or dfs(x, y - 1) or dfs(x, y + 1):
            return True

        path.pop()
        return False

    if dfs(start[0], start[1]):
        return path
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

result_path = get_maze_path(grid, start_point, end_point)
print(result_path)