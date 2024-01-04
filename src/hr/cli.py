from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser(description='Export user information to json or csv')

    parser.add_argument("--format",
            help="specify CSV to export to CSV instead of JSON"
            )
    parser.add_argument("--path",
            default='json',
            choices=['json', 'csv'],
            type=str.lower,
            help="specify path to export to a file, instead of just being displayed"
            )

    return parser

def main():

