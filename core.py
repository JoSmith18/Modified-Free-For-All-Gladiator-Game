from random import randint, choice
from termcolor import colored, cprint


def get_is_dead(fighters):
    alive = []
    for warriors in fighters:
        if warriors.health > 0:
            alive.append('{}'.format(repr(warriors)))
    return '\n'.join(alive)


def get_class():
    classes = [Ninja, SoulReaper, Saiyan]
    class_type = choice(classes)
    return class_type


def damage_finder(a, b):
    d1 = randint(a, b)
    d2 = randint(a, b)
    return min(d1, d2), max(d1, d2)


class Fighter:
    def __init__(self, fighter_type, name, damage_low, damage_high):
        self.fighter_type = fighter_type
        self.health = 100
        self.name = name
        self.damage_low = damage_low
        self.damage_high = damage_high

        rage = {'Saiyan': 60}
        self.rage = rage.get(fighter_type, 20)

    def __str__(self):
        return '{} {}| Health: {}| Rage: {}'.format(
            self.fighter_type, self.name, self.health, self.rage)

    def __repr__(self):
        return 'Fighter(Type: {}, Name: {}, Health:{}, Rage:{}, Damage_Low: {}, Damage_High: {})'.format(
            self.fighter_type, self.name, self.health, self.rage,
            self.damage_low, self.damage_high)

    def attack(self, other):
        crit_chance = self.rage
        attacks = randint(self.damage_low, self.damage_high)
        crit = False
        if crit_chance >= randint(1, 100):
            crit = True
            attacks *= 2
            other.health = max(other.health - attacks, 0)
            self.rage = 0
            message = 'CRIT Hit for {}!'.format(attacks)
            return message
        else:
            other.health = max(other.health - attacks, 0)
            self.rage = min(100, self.rage + 15)
            message = 'Hit for {}!'.format(attacks)
            return message

    def heal(self):
        message = 'You Do Not Have Enough Rage!'
        if self.rage >= 10:
            self.health = min(self.health + 5, 100)
            self.rage = max(self.rage - 10, 0)
            message = 'You Healed +5'
        return message

    def is_dead(self):
        if self.health <= 0:
            return True
        return False

    def get_choice(self, other, decision):
        if decision.title().strip() == 'a'.title().strip():
            message = self.attack(other)
            return message
        elif decision.title().strip() == 'h'.title().strip():
            message = self.heal()
            return message
        elif decision.title().strip() == 't'.title().strip():
            message = self.transform()
            return message
        elif decision.title().strip() == 's'.title().strip():
            message = self.skip()
            return message
        elif decision.title().strip() == 'j'.title().strip():
            message = self.jutsu(other)
            return message
        elif decision.title().strip() == 'r'.title().strip():
            message = self.hollow_form()
            return message

    def skip(self):
        self.rage += 30
        message = 'You Succesfully Skipped'
        return message

    def transform(self):
        message = 'You Do Not Have Enough Rage!'
        if self.rage >= 80:
            self.health += 20
            self.damage_high += 10
            self.damage_low += 10
            self.rage = 20
            message = 'Wow That Is A New Level'
            return message
        return message

    def jutsu(self, other):
        message = 'You Do Not Have Enough Rage!'
        if self.rage >= 50:
            self.health += 5
            self.damage_high += 15
            self.damage_low += 5
            self.rage = 10
            other.health -= self.damage_high
            message = 'Your Jutsu Was Succesful'
            return message
        return message

    def hollow_form(self):
        message = 'The Hollow Can Not Take Over'
        if self.health <= 25:
            self.health += 30
            self.rage += 20
            self.damage_high += 10
            self.damage_low += 5
            message = 'You Are Now On A Rampage!!!'
        return message

    def possible_actions(self):
        actions = [['', 'a', 's'], ['', '[a]ttack', '[s]kip']]
        if self.rage >= 10:
            actions[0].append('h')
            actions[1].append('[h]eal')
        if self.rage >= 80 and self.fighter_type == 'Saiyan':
            actions[0].append('t')
            actions[1].append('[t]ransform')
        if self.rage >= 40 and self.fighter_type == 'Ninja':
            actions[0].append('j')
            actions[1].append('[j]utsu')
        if self.health <= 25 and self.fighter_type == 'Soul Reaper':
            actions[0].append('r')
            actions[1].append('[r]ampage')
        return actions


class Battle:
    """ list of figthers to take part in a free for all battle """

    def __init__(self, fighters):
        '([Fighters]) -> None'
        self.fighters = fighters

    def __str__(self):
        return '\n'.join(map(str, self.fighters))

    def is_dead(self, warrior):
        self.fighters = list(filter(lambda f: f.health > 0, self.fighters))
        for fighter in self.fighters:
            if warrior == fighter:
                if fighter.health <= 0:
                    self.fighters.remove(fighter)
                    return True

    def get_target(self, warrior_name):
        for fighter in self.fighters:
            if fighter.name == warrior_name:
                return fighter

    def get_opponents(self, warrior_name):
        opponents = []
        for warrior in self.fighters:
            if warrior != warrior_name:
                opponents.append(warrior.name)
        return opponents
