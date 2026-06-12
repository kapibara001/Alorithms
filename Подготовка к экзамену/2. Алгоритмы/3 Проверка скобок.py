def check_in_code(s: str) -> bool:
    """Проверяет скобки в произвольной строке, игнорируя прочий текст."""
    pairs = {
        ')': '(', 
        ']': '[', 
        '}': '{',
        }
    opening = set(pairs.values())
    stack = []

    for ch in s:
        if ch in opening:
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False

    return not stack


print(check_in_code("def foo(a, b): return [a + b]"))  # True
print(check_in_code("if (x > 0] { ... }"))              # False