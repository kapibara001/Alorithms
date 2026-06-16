# Очень сильно походит на рекурсивный метод
def solve_maze_backtracking(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    path = []
    visited = set()

    def backtrack(r, c):
        # Базовые проверки (границы, стены, уже посещенные)
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if maze[r][c] == 1 or (r, c) in visited:
            return False

        # 1. ДЕЛАЕМ ВЫБОР (добавляем шаг в путь)
        visited.add((r, c))
        path.append((r, c))

        # Если дошли до финиша — останавливаемся
        if (r, c) == end:
            return True

        # 2. ИССЛЕДУЕМ ВАРИАНТЫ (идем в 4 стороны)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if backtrack(r + dr, c + dc):
                return True

        # 3. ОТМЕНЯЕМ ВЫБОР (бэктрекинг - зашли в тупик, удаляем шаг)
        path.pop()
        return False

    if backtrack(start[0], start[1]):
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

result_path = solve_maze_backtracking(grid, start_point, end_point)
print(result_path)