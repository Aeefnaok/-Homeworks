time = int(input('Введите количество секунд '))

hour = time // 3600
minute = (time % 3600) // 60
sec = time - ((hour * 3600) + (minute * 60))

print(f"{hour:02} : {minute:02} : {sec:02}")
