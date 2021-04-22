import random

xCh: int = random.randint(1, 100)
Ug = 0

print('______________________________')
print('Игра "Угадай число от 1 до 100"')
print('Я загадал')
while xCh != Ug:
    Ug = int(input('Введите число '))
    if Ug == 0:
        print('Вы знаете секрет :-)')
        break
    elif Ug < xCh:
        print('Угадываемое больше Вашего')
    elif Ug > xCh:
        print('Угадываемое меньше Вашего')
else:
    print('Вы угадали число', xCh)
