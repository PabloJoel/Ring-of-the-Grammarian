from Utils.ReadConfig import get_config


def create_spell(tokens, new_token, token_index):
    spell = list()
    spell.extend(tokens[:token_index])
    spell.append(new_token)
    spell.extend(tokens[token_index+1:])

    res = " "
    return res.join(spell)


class Grammarian:
    def __init__(self, config_path):
        config = get_config(config_path)['LANGUAGE CONFIG']
        language_path = config['lang_config_path']

        language_config = get_config(language_path)
        self.language_file = language_config['SOURCE']['source_file']
        self.language_alphabet = language_config['ALPHABET']['alphabet'].split(',')

    def execute(self, spell):
        tokens = spell.split(' ')   # Split the spell into tokens (words)
        new_spells = list()

        for token_index, token in enumerate(tokens):
            for char_index in range(len(token)):
                # Generate new words by modifying the token
                new_tokens = [token[:char_index] + letter + token[char_index+1:] for letter in self.language_alphabet if token[char_index] != letter]
                # Append new words to the other tokens
                new_tokens = [create_spell(tokens, new_token, token_index) for new_token in new_tokens]
                new_spells.extend(new_tokens)
        return new_spells


if __name__ == '__main__':
    grammarian = Grammarian(config_path='grammarian_config.ini')

    spells = grammarian.execute(spell='mage hand')
    print(spells)


