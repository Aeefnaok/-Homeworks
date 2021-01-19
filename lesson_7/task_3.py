class Cell:
    def __init__(self, count):
        self.count = count
        print(f'Клетка с {self.count} ячейками')

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        if (self.count - other.count) > 0:
            return self.count - other.count
        else:
            print('Разность клеток меньше нуля')
            return 0

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return self.count // other.count

    def make_order(self, line):
        return '\n'.join(['*' * line for _ in range(self.count // line)]) + \
               '\n' + '*' * (self.count % line)


a = Cell(15)
b = Cell(12)
c = Cell(a + b)
d = Cell(a - b)
e = Cell(a * b)
f = Cell(a / b)
print(a.make_order(4))
