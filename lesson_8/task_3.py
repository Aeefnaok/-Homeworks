class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Вводите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - вводить нужно только числа!")
                yes_or_not = input(f'Попробовать еще раз? Y/N ')

                if yes_or_not == 'Y' or yes_or_not == 'y':
                    print(try_except.my_input())
                elif yes_or_not == 'N' or yes_or_not == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'

try_except = Error(1)
print(try_except.my_input())
