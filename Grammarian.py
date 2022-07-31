import os

from configparser import ConfigParser


def get_config(path):
    project_path = os.getcwd()  # Path of the project
    config_path = os.path.join(project_path, path)  # Path of Config file

    config = ConfigParser()
    config.read(config_path)

    return config


def create_spell(tokens, new_token, token_index):
    spell = list()
    spell.extend(tokens[:token_index])
    spell.append(new_token)
    spell.extend(tokens[token_index+1:])

    res = " "
    return res.join(spell)

def grammarian(spell, language_file, language_alphabet):
    tokens = spell.split(' ')   # Split the spell into tokens (words)
    new_spells = list()

    for token_index, token in enumerate(tokens):
        new_tokens = list()
        for char_index in range(len(token)):
            new_tokens = [token[:char_index] + letter + token[char_index+1:] for letter in language_alphabet if token[char_index] != letter]   # Generate new words by modifying the token
            new_tokens = [create_spell(tokens, new_token, token_index) for new_token in new_tokens]             # Append new words to the other tokens
            new_spells.extend(new_tokens)
    return new_spells


if __name__ == '__main__':
    grammarian_config = get_config(path='grammarian_config.ini')
    language_path = grammarian_config.get('LANGUAGE CONFIG', 'lang_config_path')

    language_config = get_config(path=language_path)
    language_file = language_config.get('SOURCE', 'source_file')
    language_alphabet = language_config.get('ALPHABET', 'alphabet').split(',')

    spells = grammarian(spell='mage hand', language_file=language_file, language_alphabet=language_alphabet)
    print(spells)


