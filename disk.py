import core


def get_art(filename):
    with open(filename, 'r') as file:
        art = file.read()
    return art


def unlock_fighters():
    with open('fighter.txt', 'r') as file:
        file.readline()
        fighter_info = file.readlines()
    fighter_info = map(lambda i: i.split('#'), fighter_info)
    fighter_info = list(map(
        lambda l: {
            'fighter_type': l[0].strip(),
            'rage': int(l[1].strip()),
            'special': l[2].strip(),
            'possible_names': list(map(lambda s: s.strip(), l[3].strip().split(','))),
            'filename': l[4].strip()
            },
        fighter_info))

    return [
        core.Fighter_World(fighter['fighter_type'], fighter['rage'],
                           fighter['possible_names'],
                           get_art(fighter['filename']))
        for fighter in fighter_info
    ]
