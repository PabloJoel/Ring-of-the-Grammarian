import enchant

from ReadConfig import get_config


def check_missing_words(spells_path):
    """
    Utility function to look for words that are not in the dictionary.

    :param str spells_path: path to a file containing text
    :return set: set containing words that are not registered in the dictionary
    """
    with open(spells_path, 'r') as spells_file:
        spells = spells_file.read().split()

    config = get_config()
    # Create dictionary
    d = enchant.Dict(config['LANGUAGE CONFIG']['language'])
    return {spell for spell in spells if not d.check(spell)}
