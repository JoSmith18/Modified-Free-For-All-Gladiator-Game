import sys
from termcolor import colored, cprint
from core import damage_finder, Fighter, Saiyan, Ninja, SoulReaper


def my_choices(choices, choice):
    while True:
        if choice in choices:
            return choice
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
        fighter = Saiyan(name, damage_low, damage_high)
    elif fighter_type == 'Ninja':
        fighter = Ninja(name, damage_low, damage_high)
    elif fighter_type == 'Soul Reaper' or fighter_type == 'Soul':
        fighter = SoulReaper(name, damage_low, damage_high)
    setattr(fighter, 'text_color', text_color)
    setattr(fighter, 'bg_color', bg_color)
    cprint(fighter, fighter.text_color, fighter.bg_color, attrs=['bold'])
    return fighter


def main():
    fighter1 = get_fighter('red', 'on_grey')
    fighter2 = get_fighter('yellow', 'on_grey')
    hits = 0
    while True:
        cprint(repr(fighter1), fighter1.text_color)
        if type(fighter1) == Saiyan:
            choices = fighter1.possible_actions()
            choice = input(
                colored(
                    '-- [a]ttack\n-- [h]eal\n-- [t]ransform\n-- [s]kip\n>>>',
                    'blue'))
            decisions = my_choices(choices, choice)
        elif type(fighter1) == Ninja:
            choices = fighter1.possible_actions()
            choice = input(
                '-- [a]ttack\n-- [h]eal\n-- [j]utsu\n-- [s]kip\n>>>')
            decisions = my_choices(choices, choice)
        elif type(fighter1) == SoulReaper:
            choices = fighter1.possible_actions()
            choice = input(
                '-- [a]ttack\n-- [h]eal\n-- [r]ampage\n-- [s]kip\n>>>')
            decisions = my_choices(choices, choice)
        message = fighter1.get_choice(fighter2, decisions)
        cprint(message, 'blue', 'on_yellow')
        if Fighter.is_dead(fighter2):
            print('{} WINS!!'.format(fighter1.name))
            exit()

        cprint(repr(fighter2), fighter2.text_color)
        if type(fighter2) == Saiyan:
            choices = fighter2.possible_actions()
            choice = input(
                colored(
                    '-- [a]ttack\n-- [h]eal\n-- [t]ransform\n-- [s]kip\n>>>',
                    'blue'))
            decisions = my_choices(choices, choice)
        elif type(fighter2) == Ninja:
            choices = fighter2.possible_actions()
            choice = input(
                '-- [a]ttack\n-- [h]eal\n-- [j]utsu\n-- [s]kip\n>>>')
            decisions = my_choices(choices, choice)
        elif type(fighter2) == SoulReaper:
            choices = fighter2.possible_actions()
            choice = input(
                '-- [a]ttack\n-- [h]eal\n-- [r]ampage\n-- [s]kip\n>>>')
            decisions = my_choices(choices, choice)
        message = fighter2.get_choice(fighter1, decisions)
        cprint(message, 'blue', 'on_grey')
        if Fighter.is_dead(fighter1):
            print('{} WINS!!'.format(fighter2.name))
            exit()

        print('{}\n{}\n'.format(repr(fighter1), repr(fighter2)))


if __name__ == '__main__':
    main()