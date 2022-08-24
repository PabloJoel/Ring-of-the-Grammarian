import argparse


def get_commandlineparser():
    """
    Create parser to read Command Line Inputs.
    :return:
    """
    # create parser object
    parser = argparse.ArgumentParser(description="The Ring of the Grammarian in the command line")

    # defining arguments for parser object
    parser.add_argument('-f', "--file", type=str, nargs=1, metavar="file_path",
                        help="Read and transform spells from a txt file. They must be separated by new lines.")

    parser.add_argument('-s', "--spell", type=str, nargs=1, metavar="spell_name",
                        help="Transform spell from input.")

    return parser

