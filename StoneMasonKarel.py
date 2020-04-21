from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        turn_left()
        fix_arche()
        descend()
        turn_left()
        next_arche()
    turn_left()
    fix_arche()
    descend()
    turn_left()



def fix_arche():
    while front_is_clear():
        if (beepers_present()):
            move()
        else:
            put_beeper()
    if (no_beepers_present()):
        put_beeper()


def next_arche():
    for i in range(4):
        move()
def descend():
    turn_left()
    turn_left()
    while front_is_clear():
        move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
