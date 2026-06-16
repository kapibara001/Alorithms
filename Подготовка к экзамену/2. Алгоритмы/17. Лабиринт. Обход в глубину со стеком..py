def get_maze_path_stack(maze, start, end):
    """
    Обозначаем переменные rows, columns, visited, path, directions(направления(x, y)) и stack(точки старта и
    индекс направления).
    Пока наш стек не пустой:
        достаем точки x, y и индекс направления
        Если пришли в первый раз: добавление в посещенные и добавление в путь
        Если точки = точки конца - возвращаем путь
        Если просмотрели все направления (direction_index = 4), то откатываемся (stack.pop, path.pop, continue)
        Иначе пробуем другие направления dx, dy
        обновляем направление в стеке
        nx, ny = x+dx ...
        Если мы в необходимых рамках с направлениями nx, ny и точка не посещенная и не стена:
            добавляем nx, ny, 0 направление в stack
    Если ничего не вернулось - возвращаем пустой массив
    """
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

        if (0 <= nx < cols and 0 <= ny < rows and maze[ny][nx] == 0 and (nx, ny) not in visited):
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