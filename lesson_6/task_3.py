class Worker:
    def __init__(self, name, surname, position, salary, prize):
        self.n = name
        self.s = surname
        self.p = position
        self._inc = {'wage': float(salary), 'bonus': float(prize)}


class Position(Worker):

    def get_fullname(self):
        print(f'Имя, фамилия и должность сотрудника: {self.n + " " + self.s, + " " + self.p}')

    def get_totalincome(self):
        salary = self._inc['wage'] + self._inc['bonus']
        print(f'Доход сотрудника составляет {salary} y.e.')


batrak1 = Position(input('Введите имя сотрудника: '), input('Введите фамилию сотрудника: '),
                   input('Введите должность сотрудника: '), input('Введите размер оклада в y.e.: '),
                   input('Введите размер премии в y.e.: '))

batrak1.get_fullname()
batrak1.get_totalincome()
