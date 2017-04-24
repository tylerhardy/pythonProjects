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
                print('{} is not a valid choice, please choose a valid class'.format(_class))
            continue
    return hero

def encounter(player, monster):
    if monster.speed >= player.speed:
        turn = monster.name
    else:
        turn = player.name
    turns = 0
    ran_away = False
    while ran_away == False:
        print('A monster {} appeared!'.format(monster.name), 'What would you like to do? (Attack, Examine, Runaway)', end='\n')
        initial_action = input()
        if initial_action.lower() == 'Attack':            
            print('Turn {} start'.format(str(turns)))
            if player.health == 0:
                print('{} died'.format(player.name))
                break
            elif monster.health == 0:
                print('{} died'.format(monster.name))
                break
            if turn == player.name:
                print('{}\'s turn.'.format(player.name))
                print('What would you like to do? (Attack or Run)')
                attack = False
                while attack == False:
                    action = input()
                    if action.lower() == 'attack':
                        attack = True
                        break
                    elif action.lower() == 'run':
                        print('You run away from the encounter')
                        ran_away = True
                        break
                if attack:
                    print('{} attacks the monster {} for {} damage!'.format(player.name, monster.name, player.attack))
                    monster.health = monster.health - player.attack
                    print('monster {} health dropped to {}'.format(monster.name, monster.health))
                    turn = monster.name
                    turns += 1
                    continue                    
            elif turn == monster.name:
                print('{}\'s turn.'.format(monster.name))
                print('Monster {} attacks {} for {} damage!'.format(monster.name, player.name, monster.attack))
                player.health = player.health - monster.attack
                print('{}\'s health dropped to {}'.format(player.name, player.health))
                turn = player.name
                turns += 1
                continue
        elif initial_action.lower() == 'examine':
            print('{}\'s HP: {}'.format(blob.name, blob.health))
            print('{}\'s Attack: {}'.format(blob.name, blob.attack))
            print('{}\'s Defense: {}'.format(blob.name, blob.defense))
            print('{}\'s Speed: {}'.format(blob.name, blob.speed))
            continue
        elif initial_action.lower() == 'runaway':
            print('You\'ve successfully ranaway!')
            ran_away = True
            continue


hero = HeroClass()
print('Hello ' + hero.name)
print('{}\'s HP: {}'.format(hero.name, hero.health))
print('{}\'s Attack: {}'.format(hero.name, hero.attack))
print('{}\'s Defense: {}'.format(hero.name, hero.defense))
print('{}\'s Speed: {}'.format(hero.name, hero.speed))

blob = Monster('Blob')
encounter(hero,blob)