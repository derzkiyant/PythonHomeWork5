from random import randint

"""
1. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять 
первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
"""

print('Решение задачи 1:')

motion = randint(0, 1)

quantity = 2021
step = 29

while quantity >= 0:
    if motion == 0:
        player = int(
            input('Ход игрока: '))
        while player > 28 or player < 1:
            player = int(
                input('Неверный ввод. Ход игрока: '))

        quantity -= player
        if quantity <= 0:
            print('Победил игрок')
            break
        motion = 1

    else:
        if quantity < 29:
            bot = quantity
        else:
            if quantity % step == 0:
                bot = randint(1, 28)
            else:
                bot = quantity % step
        print(f'Ход бота: {bot}')

        quantity -= bot
        if quantity <= 0:
            print('Победил бот')
            break
        motion = 0

    print(f'Остаток конфет: {quantity}\n')
