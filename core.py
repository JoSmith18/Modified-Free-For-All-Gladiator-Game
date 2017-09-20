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


class Fighter_World:
    def __init__(self, fighter_type, rage, possible_names, art):
        self.fighter_type = fighter_type
        self.rage = rage
        self.possible_names = possible_names
        self.art = art


class Fighter:
    def __init__(self, fighter_world, name, damage_low, damage_high, cpu):
        self.fighter_type = fighter_world.fighter_type
        self.health = 100
        self.name = name
        self.damage_low = damage_low
        self.damage_high = damage_high
        self.rage = fighter_world.rage
        self.cpu = cpu
        self.art = fighter_world.art

        # rage = {'Mar'}
        # rage = {'Saiyan': 60}
        # self.rage = rage.get(fighter_type, 20)

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
            message = 'CRIT Hit for {} on {}'.format(attacks, other.name)
            return message
        else:
            other.health = max(other.health - attacks, 0)
            self.rage = min(100, self.rage + 15)
            message = 'Hit for {} on {}!'.format(attacks, other.name)
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

    def make_move(self, other, decision):
        if decision == 'a':
            message = self.attack(other)
            return message
        elif decision == 'h':
            message = self.heal()
            return message
        elif decision == 't':
            message = self.transform()
            return message
        elif decision == 's':
            message = self.skip()
            return message
        elif decision == 'j':
            message = self.jutsu(other)
            return message
        elif decision == 'r':
            message = self.hollow_form()
            return message
        elif decision == 'p':
            message = self.powerpunch(other)
        elif decision == 'f':
            message = self.song_attack(other)
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
            message = 'TRANSFORMED! Wow That Is A New Level!!'
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
            message = 'Your Jutsu Was Successful on {} for {} damage'.format(
                other.name, self.damage_high)
            return message
        return message

    def song_attack(self, other):
        message = 'Was Not Successful'
        if self.health <= 50:
            self.damage_low += 5
            self.damage_high += 5
            other.rage -= 40
            message = 'It Was A Success'
        return message

    def powerpunch(self, other):
        message = 'Not Enough Rage'
        if self.rage >= 60:
            other.health -= 30
            message = 'Successful Hit for 30'
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
        actions = [['a', 's', 'a', 'a', 'a', 'a', 'a'], ['[a]ttack', '[s]kip']]
        if self.rage >= 10 and self.health < 100:
            actions[0].append('h')
            actions[1].append('[h]eal')
        if self.rage >= 80 and self.fighter_type == 'Saiyan':
            actions[0].append('t')
            actions[0].append('t')
            actions[0].append('t')
            actions[0].append('t')
            actions[0].append('t')
            actions[0].append('t')
            actions[0].append('t')
            actions[0].append('t')
            actions[0].append('t')
            actions[1].append('[t]ransform')
        if self.rage >= 50 and self.fighter_type == 'Ninja':
            actions[0].append('j')
            actions[0].append('j')
            actions[0].append('j')
            actions[0].append('j')
            actions[0].append('j')
            actions[0].append('j')
            actions[0].append('j')
            actions[0].append('j')
            actions[0].append('j')
            actions[1].append('[j]utsu')
        if self.health <= 25 and self.fighter_type == 'Soul Reaper':
            actions[0].append('r')
            actions[0].append('r')
            actions[0].append('r')
            actions[0].append('r')
            actions[0].append('r')
            actions[0].append('r')
            actions[0].append('r')
            actions[1].append('[r]ampage')
        if self.rage >= 60 and self.fighter_type == 'Disney':
            actions[0].append('p')
            actions[0].append('p')
            actions[0].append('p')
            actions[0].append('p')
            actions[0].append('p')
            actions[0].append('p')
            actions[0].append('p')
            actions[0].append('p')
            actions[1].append('[p]owerpunch')
        if self.health <= 50 and self.fighter_type == 'Nickelodeon':
            actions[0].append('f')
            actions[0].append('f')
            actions[0].append('f')
            actions[0].append('f')
            actions[0].append('f')
            actions[0].append('f')
            actions[0].append('f')
            actions[1].append('[F]UN')
        return actions


class Battle:
    """ list of figthers to take part in a free for all battle """

    def __init__(self, fighters, possible_fighters):
        '([Fighters]) -> None'
        self.fighters = fighters
        self.possible_fighters = possible_fighters

    def __str__(self):
        return '\n'.join(map(str, self.fighters))

    def burythedead(self):
        ''' removes any dead warriors '''
        has_died = []
        for fighter in self.fighters:
            if fighter.health <= 0:
                has_died.append(fighter.name)
                self.fighters.remove(fighter)
        if has_died:
            return '{} has died and been removed from the arena.'.format(
                ', '.join(has_died))

    def get_target(self, warrior_name):
        for fighter in self.fighters:
            if fighter.name == warrior_name:
                return fighter
        raise ValueError('WHOOAH NELLY')

    def get_opponents(self, fighter):
        ''' returns the string names of all fighters not the attacker '''
        opponents = []
        for defender in self.fighters:
            if defender != fighter:
                opponents.append(defender)
        return opponents

    def keep_fighting(self):
        ''' returns true as long as moore than one person remains '''
        return len(self.fighters) > 1

    def get_next_fighter(self, fighter):
        """ Return The Next Attacker """
        index = 0
        if fighter:
            index = self.fighters.index(fighter) + 1
        if index >= len(self.fighters):
            index = 0
        return self.fighters[index]

    def set_possible_fighter_names(self):
        ''' -> {str: [str]} 
        returns a dicitonary of possible fighter names 
        '''
        self.possible_names = {
            warrior.fighter_type: warrior.possible_names
            for warrior in self.possible_fighters
        }

    def set_possible_fighter_types(self):
        ''' -> {str: [str]} 
        returns a dicitonary of possible fighter names 
        '''
        self.possible_types = [
            warrior.fighter_type for warrior in self.possible_fighters
        ]

    def get_fighter_world(self, fighter_type):
        for world in self.possible_fighters:
            if fighter_type == world.fighter_type:
                return world

    def get_description(self):
        for descript in self.get_fighter_world(self.fighter_type):
            return 'What Type Of Fighter Would You Like? {}-*{}'.format(
                self.possible_types, descript.description)