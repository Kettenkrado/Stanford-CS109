"""
This file lets you run the play_game function defined in the
cs109_pset1.py file. Put that file and this file in the same 
directory.

To run this file in the Pycharm terminal, or in a command
line that's pointed to the directory that houses this file, 
type:
  python3 main.py

You might have to replace python3 with py or python depending 
on your version of Python.
"""

from cs109_pset1 import play_game


def main():
    print('Your play_game function with default parameters returned', play_game())


# This if-test is True if this file was executed directly on 
# the command line. (It would be False if this file were imported
# by some other file.)
if __name__ == '__main__':
    main()
