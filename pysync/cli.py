import argparse
import sys
from pysync.pysync import PySync

def cmd_parser():
    """ Command line argument parser for the pysync entry point.
    
    Returns
    -------
    argparse.ArgumentParser
        The specified argument parser.
    """
    parser = argparse.ArgumentParser(
        usage="""%(prog)s <source> <target> [<options>]""",
        description="""Backup files from <source> to <target>""")

    # Positional (required) argument: source directory
    parser.add_argument('source',
                        help="""The directory to backup""",
                        metavar='<source>')
    
    # Positional (required) argument: target directory
    parser.add_argument('target',
                        help="""The directory to store the
                                backup of <source> to.""",
                        metavar='<target>')
    
    return parser

def pysync_io(argv):
    """ The pysync command line tool.

    Parameters
    ----------
    args: list
        output of sys.args[1:].
    """

    # Try to parse the arguments with the specified parser
    parser = cmd_parser()

    # if no arguments are specified, print the help
    if not argv:
        parser.print_help()
        sys.exit()

    # if arguments are specified, try to parse them with the defined parser
    try:
        args = parser.parse_args(argv)
    except SystemExit:
        return

    # Check input and perform respective actions
    Backup = PySync(args.source, args.target)
    Backup.sync()

def pysync():
    """ *Entry point* """

    pysync_io(sys.argv[1:])

if __name__ == '__main__':
    sys.exit(pysync())
    