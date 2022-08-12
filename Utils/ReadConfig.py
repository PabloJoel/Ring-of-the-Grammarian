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
    root_project_path = os.path.join(get_root_project_path(), 'grammarian_config.ini')

    parser = ConfigParser()
    parser.read(root_project_path, encoding='utf-8')
    return {section: dict(parser.items(section)) for section in parser.sections()}
