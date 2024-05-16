from data import *
from func import *


name = input('Ведите страну игрок ')
player['name'] = name

current_enemy = 0

while True:
    action = input('''Выбери действие:
1 - В бой!  //в разработке
2 - Информация о стране   
3 - Информация о текущем противнике  //в разработке
4 - Информация сколько хп у противника//в разработке 
5 - Тренирофка// в разработке                                     
''')
    if action == '1':
        current_enemy = fight(current_enemy)
       



 #Информация о стране 
    if action == '2':
        info_player()


#Тренировка
    if action == '5':
        training_type = input('1 - тренировать атаку, 2 - тренировать оборону')
        training(training_type)


