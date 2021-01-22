class DivisionByZero:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def divide_by_zero(x, y):
        try:
            return (x / y)
        except:
            return (f"Деление на ноль недопустимо")


div = DivisionByZero(18, 3)
print(DivisionByZero.divide_by_zero(2, 0))
print(DivisionByZero.divide_by_zero(6, 3))
print(div.divide_by_zero(18, 0))
