import enchant
from nltk.tokenize import wordpunct_tokenize

from Grammarian import Grammarian
from FileUtils import get_config


def check_missing_words(spells_path):
    """
    Utility function to look for words that are not in the dictionary.

    :param str spells_path: path to a file containing text
    :return set: set containing words that are not registered in the dictionary
    """
    gm = Grammarian()

    tokens = list()
    with open(spells_path, 'r') as spells_file:
        spells = spells_file.read().split('\n')
        for spell in spells:
            tokens.extend(wordpunct_tokenize(str.lower(spell)))

    spells = [token for token in tokens if gm.is_correct_word(token=token, regex=gm.get_alphabet_regex())]

    config = get_config()
    return {spell for spell in spells if not gm.dictionary.check(spell)}
