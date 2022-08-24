import copy
import json
import re
import enchant
from nltk.tokenize import wordpunct_tokenize

from Utils.FileUtils import get_config, get_personal_words_path
from Utils.CommandLineParser import get_commandlineparser


def put_together_spell(tokens, new_token, token_index):
    """
    Spells are splitted into tokens (words), and so, they need to be put together later. This function does that.
    It takes new_token and its index in the tokens, and replace the old token with the new one.

    :param list[str] tokens: list of tokens(words)
    :param str new_token: new token to replace the old one
    :param int token_index: index of the token in tokens
    :return:
    """
    spell = list()
    spell.extend(tokens[:token_index])
    spell.append(new_token)
    spell.extend(tokens[token_index+1:])

    res = " "
    return res.join(spell)


class Grammarian:
    def __init__(self):
        self.config = get_config()['LANGUAGE CONFIG']
        self.config['alphabets'] = json.loads(self.config['alphabets'])
        self.dictionary = enchant.DictWithPWL(
            self.config['language'],
            get_personal_words_path(language=self.config['language'])
        )

    def is_correct_word(self, token, regex):
        """
        Returns True if the token(word) can be created using regex(alphabet), otherwise False.

        :param str token: word to be checked
        :param str regex: string containing the alphabet
        :return bool:
        """
        result = re.split(regex, token)
        for elem in result:
            if elem != '':
                return False
        return True

    def get_alphabet_regex(self):
        """
        Returns string representation of the alphabet as a regular expression(regex).

        :return str:
        """
        alphabet = self.config['alphabets'][self.config['language']]

        regex = "["
        for letter in alphabet:
            regex += letter + ','
        regex = regex[:-1]
        regex += "]"

        return regex

    def create_words(self, tokens, token, current_token_index):
        """
        This function takes a token(word from the spell), iterates over the alphabet to generate all the different
        combinations and removes the ones that are not real words.

        :param list[str] tokens: list containing the words that make the spell
        :param str token: token(word) that is going to be changed
        :param int current_token_index: index of the token from tokens
        :return list[str]: list of posible spells
        """
        alphabet = copy.deepcopy(self.config['alphabets'][self.config['language']])
        alphabet.append('')

        alphabet_regex = self.get_alphabet_regex()
        is_correct_word = self.is_correct_word(token, alphabet_regex)

        if is_correct_word:
            new_spells = list()
            for char_index in range(len(token)):
                # Generate new words by modifying the token
                new_tokens = [token[:char_index] + letter + token[char_index + 1:] for letter in alphabet if
                              token[char_index] != letter]

                # Remove empty words
                new_tokens = [token for token in new_tokens if token != '']

                # Collect only real words
                new_tokens = [token for token in new_tokens if self.dictionary.check(token)]

                # Append new words to the other tokens
                new_tokens = [put_together_spell(tokens, new_token, current_token_index) for new_token in new_tokens]

                new_spells.extend(new_tokens)
            return new_spells
        else:
            return list()

    def execute(self, spell):
        """
        Main function, it takes a spell name and returns a list of changes according to the rules of
        the Ring of the Grammarian.

        :param str spell: spell name
        :return list[str]: list of posible spells
        """
        tokens = wordpunct_tokenize(str.lower(spell))  # Split the spell into tokens (words)

        new_spells = [spell]
        for token_index, token in enumerate(tokens):
            new_spells.extend(self.create_words(tokens, token, token_index))
        return new_spells

    def execute_file(self, filepath):
        """
        Reads a file from filepath. The file should contains spells separated by new lines.
        Returns the permutations for all the spells.

        :param str filepath: path to the txt cotaining the spells
        :return list[str]: list of posible spells for every spell
        """
        with open(filepath, 'r') as file:
            content = file.read().split('\n')

        spells = list()
        for spell in content:
            spells.extend(self.execute(spell=spell))
        return spells


if __name__ == '__main__':
    gm = Grammarian()

    parser = get_commandlineparser()
    args = parser.parse_args()

    if args.file is not None:
        print(gm.execute_file(args.file[0]))
    elif args.spell is not None:
        print(gm.execute(args.spell[0]))

