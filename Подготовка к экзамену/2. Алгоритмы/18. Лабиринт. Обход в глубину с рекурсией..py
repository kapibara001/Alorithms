def get_maze_path(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    path = []

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if maze[r][c] == 1 or (r, c) in visited:
            return False

        visited.add((r, c))
        path.append((r, c))

        if (r, c) == end:
            return True

        if dfs(r - 1, c) or dfs(r + 1, c) or dfs(r, c - 1) or dfs(r, c + 1):
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