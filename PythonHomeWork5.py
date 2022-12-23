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

print('\nРешение задачи 1:')

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
            print('Победил игрок!')
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
            print('Победил бот!')
            break
        motion = 0

    print(f'Остаток конфет: {quantity}\n')


"""
2. Создайте программу для игры в "Крестики-нолики".
"""

print('\nРешение задачи 2:')

moves = {'1': (0, 0), '2': (0, 1), '3': (0, 2), '4': (1, 0), '5': (1, 1),
         '6': (1, 2), '7': (2, 0), '8': (2, 1), '9': (2, 2)}


def win(k, tab):
    if (tab[0][0] == k and tab[0][1] == k and tab[0][2] == k)\
            or (tab[1][0] == k and tab[1][1] == k and tab[1][2] == k)\
            or (tab[2][0] == k and tab[2][1] == k and tab[2][2] == k)\
            or (tab[0][0] == k and tab[1][0] == k and tab[2][0] == k)\
            or (tab[0][1] == k and tab[1][1] == k and tab[2][1] == k)\
            or (tab[0][2] == k and tab[1][2] == k and tab[2][2] == k)\
            or (tab[0][0] == k and tab[1][1] == k and tab[2][2] == k)\
            or (tab[0][2] == k and tab[1][1] == k and tab[2][0] == k):
        return 1
    else:
        return 0


table = [['₁', '₂', '₃'], ['₄', '₅', '₆'], ['₇', '₈', '₉']]
for i in table:
    print(i)

motion = randint(1, 2)

for i in range(9):
    if motion == 1:
        step = input(f"\nХод 1-го игрока ('X'): ")
        table[moves[step][0]][moves[step][1]] = 'X'
        if win('X', table) == 1:
            for j in table:
                print(j)
            print('\nПобедил 1-ый игрок!')
            break
        motion = 2
    else:
        step = input(f"\nХод 2-го игрока ('0'): ")
        table[moves[step][0]][moves[step][1]] = '0'
        if win('0', table) == 1:
            for j in table:
                print(j)
            print('\nПобедил 2-ой игрок!')
            break
        motion = 1

    for j in table:
        print(j)

    if i == 8:
        print("\nНичья!")


"""
3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
"""

print("\nРезультат решения задачи 3 находится в файлах:\n'text1.txt' - начальные данные\
        \n'text2.txt '- сжатие\n'text3.txt' - восстановление")

with open('text1.txt', 'r', encoding='utf-8') as file:
    text1 = file.read()

count = 1
text2 = ''

for i in range(len(text1)-1):
    if text1[i] == text1[i+1]:
        if i != len(text1)-2:
            count += 1
        else:
            count += 1
            text2 += str(count) + text1[i]
            break
    else:
        if count == 1:
            text2 += text1[i]
        else:
            text2 += str(count) + text1[i]
        count = 1

        if i == len(text1)-2:
            text2 += text1[i+1]

with open('text2.txt', 'w', encoding='utf-8') as file:
    file.write(text2)

with open('text2.txt', 'r', encoding='utf-8') as file:
    text = file.read()

text3 = ''
count1 = -1
i = 0

while i < len(text)-1:
    if text[i].isdigit():
        count1 = int(text[i])
        text3 += text[i+1] * count1
        i += 2
    else:
        text3 += text[i]
        i += 1
        if i == len(text)-1:
            text3 += text[i]

with open('text3.txt', 'w', encoding='utf-8') as file:
    file.write(text3)
