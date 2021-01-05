class Car:

    def __init__(self, speed, color, name, is_police):
        self.s = int(speed)
        self.c = color
        self.n = name
        self.pol = is_police

    def go(self):
        print(f'Машина {self.n} поехала!')

    def stop(self):
        print(f'Машина {self.n} остановилась')

    def turn(self):
        direction = input(f'Если машина {self.n} повернула, то в какую сторону? ').lower()
        if direction == 'налево':
            print(f'Машина {self.n} повернула налево')
        elif direction == 'направо':
            print(f'Машина {self.n} повернула направо')
        else:
            print(f'Машина {self.n} никуда не сворачивала')

    def show_speed(self):
        print(f'Текущая скорость машины {self.n}: {self.s} км/ч')


class TownCar(Car):

    def whois(self):
        print(f'Это городской автомобиль {self.n}')


    def show_speed(self):
        if self.s > 60:
            print(f'Сейчас кто-то схлопочет штраф за превышение скорости!! Текущая скорость машины {self.n}: {self.s} км/ч')
        else:
            print(f'Машина {self.n} движется с нормальной скоростью: {self.s} км/ч')


class SportCar(Car):

    def whois(self):
        print(f'Это здоровский спорткар! {self.n}')


class WorkCar(Car):

    def whois(self):
        print(f'На этом {self.n} только на работу ездить')

    def show_speed(self):
        if self.s > 40:
            print(f'Сейчас кто-то схлопочет штраф за превышение скорости!! Текущая скорость машины {self.n}: {self.s} км/ч')
        else:
            print(f'Машина {self.n} движется с нормальной скоростью: {self.s} км/ч')


class PoliceCar(Car):

    def whois(self):
        print(f'Этот автомобиль {self.n} принадлежит полиции ')


car1 = TownCar(input('Введите скорость машины: '), input('Введите цвет машины: '),
               input('Введите название машины: '), input('Эта машина принадлежит полиции? '))

car1.whois()
car1.go()
car1.stop()
car1.turn()
car1.show_speed()

car2 = SportCar(input('Введите скорость машины: '), input('Введите цвет машины: '),
               input('Введите название машины: '), input('Эта машина принадлежит полиции? '))

car2.whois()
car2.go()
car2.stop()
car2.turn()
car2.show_speed()

car3 = WorkCar(input('Введите скорость машины: '), input('Введите цвет машины: '),
               input('Введите название машины: '), input('Эта машина принадлежит полиции? '))

car3.whois()
car3.go()
car3.stop()
car3.turn()
car3.show_speed()

car4 = PoliceCar(input('Введите скорость машины: '), input('Введите цвет машины: '),
               input('Введите название машины: '), input('Эта машина принадлежит полиции? '))

car4.whois()
car4.go()
car4.stop()
car4.turn()
car4.show_speed()
