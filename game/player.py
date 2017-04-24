import random

class Warrior:
    def __init__(self):
        self.name = 'Warrior'
        self.health = 100
        self.attack = 10
        self.defense = 10
        self.speed = 6

class Rogue:
    def __init__(self):
        self.name = 'Rogue'
        self.health = 80
        self.attack = 15
        self.defense = 7
        self.speed = 7

class Wizzard:
    def __init__(self):
        self.name = 'Wizzard'
        self.health = 50
        self.attack = 20
        self.defense = 5
        self.speed = 4

class Monster:
    def __init__(self,name):
        self.name = name
        self.health = random.randint(1, 100)
        self.attack = random.randint(1, 20)
        self.defense = random.randint(1, 10)
        self.speed = random.randint(1, 10)

def HeroClass():
    print('What class would you like to be? (Warrior, Rogue, or Wizzard)')
    while True:
        _class = input()
        if _class.lower() == 'warrior':
            hero = Warrior()
            break
        elif _class.lower() == 'rogue':
            hero = Rogue()
            break
        elif _class.lower() == 'wizzard':
            hero = Wizzard()
            break
        else:
            if _class == "":
                print('Please input a class.')
            else:
                print('{0} is not a valid choice, please choose a valid class'.format(_class))
            continue
    return hero

def encounter(player, monster):
    turns = 1
    ran_away = False
    print('A monster {0} appeared!'.format(monster.name))
    if monster.speed >= player.speed:
        print('The monster {} has started the encounter!'.format(monster.name))
        print('Turn {0}, {1}\'s turn!'.format(str(turns), monster.name))
        turn = monster.name
    else:
        print('Turn {0}, {1}\'s turn!'.format(str(turns), player.name))
        turn = player.name
    while ran_away == False:
        if turn == player.name:
            print('What would you like to do? (Attack, Examine, Runaway)')
            action = input()
            if action.lower() == 'attack':   
                print('{0} attacks the monster {1} for {2} damage!'.format(player.name, monster.name, player.attack))
                monster.health = monster.health - player.attack
                print('monster {0} health dropped to {1}.'.format(monster.name, monster.health))
                if monster.health <= 0:
                    print('{0} was defeated!'.format(monster.name))
                    break
                turn = monster.name
                turns += 1
            elif action.lower() == 'examine':
                print('{0}\'s HP: {1}'.format(blob.name, blob.health))
                print('{0}\'s Attack: {1}'.format(blob.name, blob.attack))
                print('{0}\'s Defense: {1}'.format(blob.name, blob.defense))
                print('{0}\'s Speed: {1}'.format(blob.name, blob.speed))
            elif action.lower() == 'runaway':
                print('You\'ve successfully ranaway!')
                ran_away = True
        elif turn == monster.name:
            print('Monster {0} attacks {1} for {2} damage!'.format(monster.name, player.name, monster.attack))
            player.health = player.health - monster.attack
            print('{0}\'s health dropped to {1}.'.format(player.name, player.health))
            if player.health <= 0:
                print('{0} has died!'.format(player.name))
                break
            turn = player.name
            turns += 1



hero = HeroClass()
print('Hello ' + hero.name)
print('{0}\'s HP: {1}'.format(hero.name, hero.health))
print('{0}\'s Attack: {1}'.format(hero.name, hero.attack))
print('{0}\'s Defense: {1}'.format(hero.name, hero.defense))
print('{0}\'s Speed: {1}'.format(hero.name, hero.speed))

blob = Monster('Blob')
encounter(hero,blob)