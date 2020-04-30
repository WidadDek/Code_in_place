"""
File: nimm.py
-------------------------
Add your comments here.
"""

NUM_STONES = 20


def main():
    cpt = NUM_STONES
    player_num = 1
    while cpt != 0:
        print("There are " + str(cpt) + " stones left")
        to_remove = int(input("Player " + str(player_num) + " would you like to remove 1 or 2 stones? "))
        if player_num == 1:
            player_num = 2
        else:
            player_num = 1
        while to_remove < 1 or to_remove > 2:
            to_remove = int(input("Please enter 1 or 2: "))
        print('')

        cpt -= to_remove
    print("Player " + str(player_num) + " wins!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
