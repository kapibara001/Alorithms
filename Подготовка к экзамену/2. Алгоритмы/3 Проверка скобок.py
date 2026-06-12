def check_pairs(s):
    """Алгоритм проверки скобок. Делается просто проверкой ключей и значений"""
    pairs = {
        '}': '{',
        ')': '(',
        ']': '[',
    }
    openings = pairs.values()
    stack = []

    for ch in s:
        if ch in openings:
            stack.append(ch)
        elif ch not in openings:
            if stack.pop() != pairs[ch]:
                return False

    return not stack


string = '[()()]{}'
print(check_pairs(string))