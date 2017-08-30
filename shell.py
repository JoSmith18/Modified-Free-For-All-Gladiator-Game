import sys, disk
from termcolor import colored, cprint
from core import damage_finder, Fighter, get_class, get_is_dead, Battle, Fighter_World
from random import choice, randint
from time import sleep


def get_cpu(battle):
    fighter_type = choice(list(battle.possible_names.keys()))
    world = battle.get_fighter_world(fighter_type)
    damage_low, damage_high = damage_finder(10, 25)
    name = battle.possible_names[fighter_type].pop(
        randint(0, len(battle.possible_names[fighter_type]) - 1))
    if len(battle.possible_names[fighter_type]) == 0:
        battle.possible_names.pop(fighter_type)
    fighter = Fighter(world, name, damage_low, damage_high, True)
    cprint(fighter, 'green', 'on_grey')
    return fighter


def get_fighter(battle, text_color, bg_color):
    print(
        colored(
            '\nWhat Type Of Fighter Would You Like:?\n Saiyan- Starts With Rage Of 60 And Has The Ability To Transform At Rage 90!\n SoulReaper - Starts with rage at 25, and when health gets 25 or lower can rampage which increases his stats!\n Ninja - Starts With Rage 20 And At Rage 50 Can Do A Special Jutsu!\n Disney- Cute Cartoon that starts with major RAGE!!!\n Nickelodeon - Has The Ability When Health Gets To Half To Calm Another Fighter Rage Down!\n',
            'red', 'on_white'),
        end="")
    fighter_type = ''
    while fighter_type not in battle.possible_types:
        print(colored('>>>', 'yellow', attrs=['blink']), end="")
        fighter_type = input(' ').title()
    world = battle.get_fighter_world(fighter_type)
    name = input("What Is Your Name Fighter: ")
    damage_low, damage_high = damage_finder(10, 25)
    fighter = Fighter(world, name, damage_low, damage_high, False)
    setattr(fighter, 'text_color', text_color)
    setattr(fighter, 'bg_color', bg_color)
    cprint(fighter, fighter.text_color, fighter.bg_color, attrs=['bold'])
    return fighter


def amount_of_fighters(battle):
    fighters = []
    while True:
        Vs = input("Will The Fighter Be An AI or Human? enter 'done' to stop\n"
                   ).title().strip()
        if Vs == 'Ai':
            if len(battle.possible_names) > 0:
                current_fighter = get_cpu(battle)
                fighters.append(current_fighter)
            else:
                print('no more AI fighters available')
                continue
        elif Vs == 'Human' [0:len(Vs)]:
            current_fighter = get_fighter(battle, 'red', 'on_grey')
            fighters.append(current_fighter)
        elif Vs == 'Done' [0:len(Vs)] and len(fighters) > 1:
            break
    return fighters


def get_move(attacker):
    moves = attacker.possible_actions()
    cprint('\n'.join(map(lambda s: '-- {}'.format(s), moves[1])), 'yellow')
    while True:
        cprint('>>> {}:'.format(attacker.name), end='')
        move = input(' ')
        if move in moves[0]:
            if move in ['a', 'j', 'f', 'p']:
                return move, True
            else:
                return move, None
        else:
            print('invalid choice')


def get_enemy(opponents, name):
    opponent_names = list(map(lambda o: o.name, opponents))
    print('\n'.join(map(lambda s: '-- {}'.format(s), opponent_names)))
    while True:
        enemy = input('{} >>> '.format(name))
        if enemy in opponent_names:
            return enemy
        print('invalid choice')


def decide_move(attacker, opponents):
    if attacker.cpu:
        cprint('{} is thinking...'.format(attacker.name), 'yellow')
        sleep(1.5)
        return choice(opponents).name, choice(attacker.possible_actions()[0])
    move, enemy = get_move(attacker)
    if enemy:
        if len(opponents) < 2:
            print('Attack >>> {}'.format(opponents[0].name))
            enemy = opponents[0].name
        else:
            enemy = get_enemy(opponents, attacker.name)
    return enemy, move.lower()


def main():
    battle = Battle([], disk.unlock_fighters())
    battle.set_possible_fighter_names()
    battle.set_possible_fighter_types()
    battle.fighters = amount_of_fighters(battle)
    print(battle, end='\n\n')
    attacker = None
    while battle.keep_fighting():
        attacker = battle.get_next_fighter(attacker)
        cprint(attacker, 'red', 'on_white')
        opponents = battle.get_opponents(attacker)
        enemy, move = decide_move(attacker, opponents)
        if enemy:
            enemy = battle.get_target(enemy)
        cprint(attacker.make_move(enemy, move.lower()), 'blue', 'on_grey')
        s = battle.burythedead()
        if s:
            cprint(s, 'red')
    cprint(
        '*********************************************************',
        'green',
        attrs=['reverse'])
    cprint(battle.fighters[0].art, 'green')
    cprint('{} WINS'.format(battle.fighters[0].name), 'green', attrs=['blink'])
    cprint(
        '*********************************************************',
        'green',
        attrs=['reverse'])
    exit()


if __name__ == '__main__':
    main()