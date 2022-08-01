from configparser import ConfigParser


def get_config(config_path):
    """
    Read ini file and return it as a dictionary. The dictionary contains as many keys as there are headers
    in the ini file. The values are dictionaries containing that header information.

    :param str config_path: path to the ini file
    :return dict: configuration
    """
    parser = ConfigParser()
    parser.read(config_path)
    return {section: dict(parser.items(section)) for section in parser.sections()}

