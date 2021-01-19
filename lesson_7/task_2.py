from abc import ABC, abstractmethod


class Clothes(ABC):
    total = 0

    @abstractmethod
    def expense(self):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        self.name = name
        self.v = v

    @property
    def expense(self):
        result = self.v / 6.5 + 0.5
        Clothes.total += result
        return f'Расход ткани на пальто {self.name}: {result:.2f}'


class Costume(Clothes):
    def __init__(self, name, h):
        self.name = name
        self.h = h

    @property
    def expense(self):
        result = 2 * self.h + 0.3
        Clothes.total += result
        return f'Расход ткани на костюм {self.name}: {result:.2f}'


a = Coat('Кромби', 256)
print(a.expense)
b = Costume('HENDERSON', 172)
print(b.expense)
print(f'Общий расход ткани: {Clothes.total:.2f}')
