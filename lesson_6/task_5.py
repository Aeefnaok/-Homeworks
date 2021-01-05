class Stationery:

    def draw(self):
        title = 'Запуск'
        print(f'{title} отрисовки')


class Pen(Stationery):
    def draw(self):
        title = 'ручки'
        print(f'Подписать документ с помощью {title}')


class Pencil(Stationery):

    def draw(self):
        title = 'карандашом'
        print(f'Вычертить чертеж {title}')


class Handle(Stationery):

    def draw(self):
        title = 'маркером'
        print(f'Выделить условные обозначения {title}')


paper0 = Stationery()
paper0.draw()

paper1 = Pen()
paper1.draw()

paper2 = Pencil()
paper2.draw()

paper3 = Handle()
paper3.draw()
