def get_maze_path_bfs(maze, start, end):
    """
    Достаем длину и ширину лабиринта, очередь с начальной точкой [start], посещенные точки с start, направления
    Пока наша очередь не пуста:
        Берем первую запись из очереди
        Получаем x, y из нее
        Если точка конечная - возврат действующего пути
        Если нет - пробуем идти в других направлениях
        Если мы находимся в нужных рамках:
            Добавляем новую точку (после нового направления) в посещенные
            Создаем новый путь и добавляем туда новые nx ny
            добавляем в очередь новый путь
    Иначе возвращаем []
    """
    rows, cols = len(maze), len(maze[0])
    visited = {start}
    queue = [[start]]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        current_path = queue.pop(0)
        x, y = current_path[-1]

        if (x, y) == end:
            return current_path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= ny < rows and 0 <= nx < cols and maze[ny][nx] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                new_path = list(current_path)
                new_path.append((nx, ny))
                queue.append(new_path)

    return []

# Пример использования:
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

print(get_maze_path_bfs(grid, (0, 0), (4, 4)))