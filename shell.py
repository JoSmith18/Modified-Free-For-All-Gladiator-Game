from core import damage_finder, Fighter, Saiyan, Ninja


def my_choices():
    choices = ['attack', 'heal']
    while True:
        choice = input('-- attack\n-- heal\n>>>')
        if choice in choices:
            return choice
        else:
            print('invalid choice')


def saiyan_choices():
    choices = ['attack', 'a', 'h', 'heal', 't', 'transform', 's', 'skip']
    while True:
        choice = input(
            '-- [a]ttack\n-- [h]eal\n-- [t]ransform\n-- [s]kip\n>>>')
        if choice in choices:
            return choice
        else:
            print('invalid choice')


def ninja_choices():
    choices = ['attack', 'a', 'h', 'heal', 'j', 'jutsu', 's', 'skip']
    while True:
        choice = input('-- [a]ttack\n-- [h]eal\n-- [j]utsu\n-- [s]kip\n>>>')
        if choice in choices:
            return choice
        else:
            print('invalid choice')


fighter_type = input('What Type Of Fighter Would You Like: Saiyan or Ninja?\n')
name = input("What Is Your Name Fighter: ")
damage_low, damage_high = damage_finder(10, 25)
if fighter_type == 'Saiyan':
    fighter1 = Saiyan(name, damage_low, damage_high)
elif fighter_type == 'Ninja':
    fighter1 = Ninja(name, damage_low, damage_high)
print(fighter1)
fighter_type2 = input(
    'What Type Of Fighter Would You Like: Saiyan or Ninja?\n')
name = input("What Is Your Name Fighter: ")
damage_low, damage_high = damage_finder(10, 25)
if fighter_type2 == 'Saiyan':
    fighter2 = Saiyan(name, damage_low, damage_high)
elif fighter_type2 == 'Ninja':
    fighter2 = Ninja(name, damage_low, damage_high)
print(fighter2)
print()
hits = 0
while True:
    print(repr(fighter1))
    if type(fighter1) == Saiyan:
        decisions = saiyan_choices()
    elif type(fighter1) == Ninja:
        decisions = ninja_choices()
    else:
        decisions = my_choices()
    message = fighter1.get_choice(fighter2, decisions)
    print(message)
    if Fighter.is_dead(fighter2):
        print('{} WINS!!'.format(fighter1.name))
        exit()

    print(repr(fighter2))
    if type(fighter2) == Saiyan:
        decisions = saiyan_choices()
    elif type(fighter2) == Ninja:
        decisions = ninja_choices()
    else:
        decisions = my_choices()
    message = fighter2.get_choice(fighter1, decisions)
    print(message)
    if Fighter.is_dead(fighter1):
        print('{} WINS!!'.format(fighter2.name))
        exit()

    print('{}\n{}\n'.format(repr(fighter1), repr(fighter2)))