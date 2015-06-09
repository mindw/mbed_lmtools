#!/usr/bin/env python


import os
import sys
import optparse
import platform

from lmtools.lmtools_win7 import LmToolsWin7
from lmtools.lmtools_ubuntu import LmToolsUbuntu

def lmtools_factory():
    """ Factory producing lmtools depending on OS it is working on
    """
    result = None
    os_info = lmtools_os_info()
    if (os_info[0] == 'nt' and os_info[1] == 'Windows'):
        result = LmToolsWin7()
    elif (os_info[0] == 'posix' and os_info[1] == 'Linux' and ('Ubuntu' in os_info[3])):
        result = LmToolsUbuntu()
    return result

def lmtools_os_info():
    """ Returns information about running OS
    """
    result = (os.name,
              platform.system(),
              platform.release(),
              platform.version(),
              sys.platform)
    return result

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

    opts, args = parser.parse_args()
    return opts, args

def main():
    opts, args = cmd_parser_setup()
    lmtools = lmtools_factory()
    lmtools.load_mbed_description()
    
    print lmtools.get_string(border=not opts.simple, header=not opts.simple)

if __name__ == '__main__':
    main()
