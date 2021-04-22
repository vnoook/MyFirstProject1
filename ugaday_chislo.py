import random

xCh = random.randint(1, 100)
Ug = 0

print('___________________________')
print('Игра "Угадай число"')
print('Я загадал число от 1 до 100\n')

while xCh != Ug:
    input_data = input('Введите число: ')
    Ug = int(input_data)

    if Ug == 0:
        print('Вы знаете секрет :-)')
        break
    elif Ug < xCh:
        print('Угадываемое больше Вашего')
    elif Ug > xCh:
        print('Угадываемое меньше Вашего')
else:
    print('Вы угадали число!!!', xCh)

print()
print('__________!МОЛОДЕЦ!___________')
