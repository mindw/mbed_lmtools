#!/usr/bin/env python

import optparse
from lmtools import lmtools_factory

def cmd_parser_setup():
    """ Configure command line options
    """
    parser = optparse.OptionParser()

    parser.add_option('-s', '--simple',
                      dest='simple',
                      default=False,
                      action="store_true",
                      help='Verbose mode (prints some extra information)')

    parser.add_option('-v', '--verbose',
                      dest='verbose',
                      default=False,
                      action="store_true",
                      help='Verbose mode (prints some extra information)')

    (opts, args) = parser.parse_args()
    return (opts, args)

"""
#lm = lmtools.list_mbeds()
"""

if __name__ == '__main__':
    (opts, args) = cmd_parser_setup()

    lmtools = lmtools_factory()
    lmtools.load_mbed_description('meta/targets.json')

    print lmtools.get_string(border=not opts.simple, header=not opts.simple)
