from dice import *
from pool import *
import sys, re

def get_all_eote_dice():
    """Returns a dict of all the dice in the Edge of the Empire game."""
    ddict = {
        'Boost': Dice('Boost', ['', '', 'Success', ['Success', 'Advantage'], ['Advantage', 'Advantage'], 'Advantage']),
        'Setback': Dice('Setback', ['', '', 'Failure', 'Failure', 'Threat', 'Threat']),
        'Ability': Dice('Ability', ['', 'Success', 'Success', ['Success', 'Success'], 'Advantage', 'Advantage', ['Advantage', 'Success'], ['Advantage', 'Advantage']]),
        'Difficulty':Dice('Difficulty', ['', 'Failure', ['Failure', 'Failure'], 'Threat', 'Threat', 'Threat', ['Threat', 'Threat'], ['Failure', 'Threat']]),
        'Proficiency': Dice('Proficiency', ['', 'Success', 'Success', ['Success', 'Success'], ['Success', 'Success'], 'Advantage', ['Success', 'Advantage'], ['Success', 'Advantage'], ['Success', 'Advantage'], ['Advantage', 'Advantage'], ['Advantage', 'Advantage'], 'Triumph']),
        'Challenge': Dice('Challenge', ['', 'Failure', 'Failure', ['Failure', 'Failure'], ['Failure', 'Failure'], 'Threat', 'Threat', ['Failure', 'Threat'], ['Failure', 'Threat'], ['Threat', 'Threat'], ['Threat', 'Threat'], 'Despair' ]),
        'Force': Dice('Force', ['Dark', 'Dark', 'Dark', 'Dark', 'Dark', 'Dark', ['Dark', 'Dark'], 'Light', 'Light', ['Light', 'Light'], ['Light', 'Light'], ['Light', 'Light']])
    }

    return ddict

def pprint_roll(roll):
    """Takes the result of a DicePool roll and prettily prints it"""
    result_count = {
        'Success': 0,
        'Failure': 0,
        'Advantage': 0,
        'Threat': 0,
        'Triumph': 0,
        'Despair': 0
    }

    for result in roll:
        if type(result) is list:
            for item in result:
                result_count[item] += 1
        elif result in result_count:
            result_count[result] += 1

    for item in result_count:
        if result_count[item] > 0:
            print '%s: %d' % (item, result_count[item])

def main():
    dice_dict = get_all_eote_dice()

    dicePool = DicePool()

    pool_str = sys.argv[1]
    matches = re.findall('[0-9]+[a-z]+', pool_str)

    dice_type_abbrev = {'b': 'Boost', 's': 'Setback', 'a': 'Ability', 'd': 'Difficulty', 'p': 'Proficiency', 'c': 'Challenge', 'f': 'Force'}

    for match in matches:
        num_dice = match[0]
        dice_type = match[1]

        if dice_type not in dice_type_abbrev:
            raise KeyError('Dice type {} not in database'.format(dice_type))

        for i in range(int(num_dice)):
            dicePool.add_dice(dice_dict[dice_type_abbrev[dice_type]])

    pprint_roll(dicePool.roll())

if __name__ == '__main__':
    main()
