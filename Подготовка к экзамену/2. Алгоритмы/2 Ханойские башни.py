def hanoi(n, source='A', target='C', aux='B', moves=None):
    """
    Рекурсивное решение задачи о Ханойских башнях.
    Возвращает список ходов в виде кортежей (from, to).
    """
    if moves is None:
        moves = []

    if n == 0:
        return moves

    # Шаг 1: переносим n-1 дисков на вспомогательный стержень
    hanoi(n - 1, source, aux, target, moves)

    # Шаг 2: переносим самый большой диск на целевой стержень
    moves.append((source, target))

    # Шаг 3: переносим n-1 дисков со вспомогательного на целевой
    hanoi(n - 1, aux, target, source, moves)

    return moves

# Пример
moves = hanoi(3)
for i, (f, t) in enumerate(moves, 1):
    print(f"{i}. {f} -> {t}")
    
        
# ИЛИ


def hanoi(a, b, c, n):
    if n == 1:
        print(a, "->", c)
    else:
        hanoi(a, c, b, n-1)
        print(a, "->", c)
        hanoi(b, a, c, n-1)
    

hanoi("A", "B", "C", 6)