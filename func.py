from data import *
def fight(cm):
    enemy = enemies[cm]
    while player['hp']>0 and enemy['hp']>0:
            
            player['hp'] -= enemy['attack']
            enemy['hp'] -= player['attack']
            
            print(f'Здоровье игрока = {player["hp"]}, Враг нанёс {enemy["attack"]} урона')
            print(f'Здоровье врага = {enemy["hp"]}')

            print()
            sleep(1.5)


    




def info_player():
 
    print(f'Страна-{player["name"]}')
    print(f'здоровье-{player["hp"]}')
    print(f'урон - {player["attack"]}')

#Тренировка 
def training(training_type):
    pass
 
 
 
def fight(current_enemy0):
     enemy = enemies[current_enemy0]
    