from configparser import ConfigParser
from pathlib import Path
import os.path


def get_root_project_path():
    """
    Returns the root path of the project

    :return str: project root path
    """
    return str(Path(__file__).parent.parent)


def get_config():
    """
    Read ini file and return it as a dictionary. The dictionary contains as many keys as there are headers
    in the ini file. The values are dictionaries containing that header information.

    :return dict: configuration
    """
    config_path = os.path.join(get_root_project_path(), 'grammarian_config.ini')

    parser = ConfigParser()
    parser.read(config_path, encoding='utf-8')
    return {section: dict(parser.items(section)) for section in parser.sections()}


def get_personal_words_path(language):
    personal_words_path = os.path.join(get_root_project_path(), 'PersonalWords')

    personal_words_all_path = os.path.join(personal_words_path, 'all.txt')
    personal_words_language_path = os.path.join(personal_words_path, f'{language}.txt')

    personal_words_path = os.path.join(personal_words_path, 'generated')
    personal_words_path = os.path.join(personal_words_path, f'{language}_generated.txt')

    with open(personal_words_all_path, "r", encoding='utf-8') as personal_words_all_file:
        personal_words_all = personal_words_all_file.read()

    with open(personal_words_language_path, 'r', encoding='utf-8') as personal_words_language_file:
        personal_words_language = personal_words_language_file.read()

    with open(personal_words_path, 'w', encoding='utf-8') as personal_words_file:
        personal_words_file.write(personal_words_all.lower())
        personal_words_file.write('\n')
        personal_words_file.write(personal_words_language.lower())

    return personal_words_path
