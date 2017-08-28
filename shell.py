import sys
from termcolor import colored, cprint
from core import damage_finder, Fighter, get_class, get_is_dead, Battle
from random import choice


def my_choices(choices, name):
    while True:
        print('\n-- '.join(choices[1]))
        choice = input('>>> {}: '.format(name))
        if choice in choices[0]:
            if choice in ['a', 'j']:
                return choice, True
            else:
                return choice, False
        else:
            print('invalid choice')


def get_fighter(text_color, bg_color):
    print(
        colored(
            '\nWhat Type Of Fighter Would You Like: Saiyan, SoulReaper, or Ninja?\n Saiyan- Starts With Rage Of 60 And Has The Ability To Transform At Rage 90!\n SoulReaper - Starts with rage at 25, and when health gets 25 or lower can rampage which increases his stats!\n Ninja - Starts With Rage 20 And At Rage 50 Can Do A Special Jutsu!\n',
            'yellow'),
        end="")
    fighter_type = ''
    while fighter_type not in ['Saiyan', 'Soul Reaper', 'Ninja', 'Soul']:
        print(colored('>>>', 'yellow', attrs=['blink']), end="")
        fighter_type = input(' ').title()
    name = input("What Is Your Name Fighter: ")
    damage_low, damage_high = damage_finder(10, 25)
    if fighter_type == 'Saiyan':
        fighter = Fighter('Saiyan', name, damage_low, damage_high)
    elif fighter_type == 'Ninja':
        fighter = Fighter('Ninja', name, damage_low, damage_high)
    elif fighter_type == 'Soul Reaper' or fighter_type == 'Soul':
        fighter = Fighter('Soul Reaper', name, damage_low, damage_high)
    setattr(fighter, 'text_color', text_color)
    setattr(fighter, 'bg_color', bg_color)
    cprint(fighter, fighter.text_color, fighter.bg_color, attrs=['bold'])
    return fighter


def amount_of_fighters():
    fighters = []
    while True:
        current_fighter = get_fighter('red', 'on_grey')
        fighters.append(current_fighter)
        answer = input(
            colored('Is That The Last Fighter?\n', 'blue',
                    'on_grey')).title().strip()
        if answer == 'Yes' or answer == 'Y':
            return fighters


def get_enemy(opponents):
    while True:
        enemy = input(
            colored('Who Would You Like To Attack:\n{}\n'.format(
                '\n'.join(opponents))))
        if enemy in opponents:
            return enemy
        print('invalid choice')


def get_fighters():
    fighters = []
    damage_low, damage_high = damage_finder(10, 25)
    fighters.append(Fighter('Saiyan', 'Jo', damage_low, damage_high))
    damage_low, damage_high = damage_finder(10, 25)
    fighters.append(Fighter('Ninja', 'Bob', damage_low, damage_high))
    damage_low, damage_high = damage_finder(10, 25)
    fighters.append(Fighter('Soul Reaper', 'Tom', damage_low, damage_high))
    return fighters


def main():
    battle = Battle(amount_of_fighters())
    print(battle)
    while True:
        for warrior in battle.fighters:
            if warrior.health <= 0:
                continue
            cprint(warrior, 'red', 'on_white')
            decisions, need_opponent = my_choices(warrior.possible_actions(),
                                                  warrior.name)
            enemy = None
            if need_opponent:
                opponents = battle.get_opponents(warrior)
                if len(opponents) > 1:
                    enemy_name = get_enemy(opponents)
                else:
                    enemy_name = opponents[0]
                enemy = battle.get_target(enemy_name)
            cprint(warrior.get_choice(enemy, decisions), 'blue', 'on_grey')
            if battle.is_dead(enemy):
                print(enemy_name, 'is dead...')
        if len(battle.fighters) == 1:
            print('{} WINS'.format(battle.fighters[0].name))
            exit()


if __name__ == '__main__':
    main()