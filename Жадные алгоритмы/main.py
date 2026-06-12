""" Задача про время, затрачиваемое на работу и вознаграждение. Надо выьрать оптимальный маршрут работ
class Task():
    def __init__(self, cost):
        self.cost = cost

    
# Жадный алгоритм потому что берем самые большие элементы и выходим когда надо, не выполняя лишней работы
# Данная задача про монеты не имеет правильного жадного решения
def solve(tasks: list[Task], k):
    tasks = sorted(tasks, key=lambda c: c.cost, reverse=True)
    sum = 0

    for i in range(k):
        if i >= len(tasks):
            break

        sum += tasks[i].cost

    return sum


p1 = Task(52)
p2 = Task(53)
p3 = Task(124)
p4 = Task(14)

funcList = [p1, p2, p3, p4]
print(solve(funcList, 15))
"""


""" Задача про полоски. Начало не может быть раньше конца предыдущей
class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    

def solve(lineList: list[Line]):
    if len(lineList) == 0:
        return 0, []
    
    lineList = sorted(lineList, key=lambda l: l.end)

    ans = 1
    res = [(lineList[0].start, lineList[0].end)]
    last_e = lineList[0].end

    for i in range(1, len(lineList)):
        if lineList[i].start >= last_e:
            ans += 1
            res.append((lineList[i].start, lineList[i].end))
            last_e = lineList[i].end
    
    return ans, res


p1 = Line(1, 3)
p2 = Line(4, 5)
p3 = Line(4, 14)
p4 = Line(9, 10)

# lineDict = [p1, p2, p3, p4]
lineDict = []

print(solve(lineDict))
"""


""" Задача про коробки. Ставим коробки друг на друга, коробка выдерживает определенный 
вес сверху и сама сколько то весит. Найти решение такой задачи. 


class Box:
    def __init__(self, weight, maxMass):
        self.weight = weight
        self.maxMass = maxMass


def solveBoxes(boxList: list[Box]):
    sumWeight = 0
    boxList = sorted(boxList, key=lambda b: ())

    ????????
"""



""" Жадный алгоритм Хаффмана. Нужен для однозначного двоичного кодирования букв
    Алгоритм:
        Слово: abracadabra
        {a, b, r, c, d} буквы в слове
        {5, 2, 2, 1, 1} колличество букв в тексте

        a   b   r   d   c
        5   2   2   1   1
        |   |   |   |   |
        |0  |1  |1  |1  |0
        |   |   |   |   |
        |   |   | 0 |---
        |   | 0 |---cd
        |   |---rcd 2
        |   |   4
        | 1 |
        |---brcd
        |   6
        abrcd
        11

        abracadabra: a:0 b:11 r:101 d:1001 c:1000

"""