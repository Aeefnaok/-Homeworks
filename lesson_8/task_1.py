class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []
        for i in day_month_year.split():
            if i != '-': my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'True'
                else:
                    return f'False'
            else:
                return f'False'
        else:
            return f'False'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('22 - 01 - 2021')
print(today)
print(Data.valid(19, 12, 2009))
print(today.valid(23, 10, 2050))
print(Data.extract('10 - 10 - 2010'))
print(today.extract('24 - 01 - 2021'))
print(Data.valid(12, 11, 1995))
