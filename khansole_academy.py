"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random

CORRECT_ANSWERS = 3
MIN_RANDOM = 10
MAX_RANDOM = 99
def main():
    cpt = 0
    while (cpt < CORRECT_ANSWERS):
        num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
        num2 = random.randint(MIN_RANDOM, MAX_RANDOM)
        correct = num1 + num2
        print('What is ' + str(num1) + '+' + str(num2) + '?')
        answer = int(input('Your answer: '))
        print(str(answer))
        if answer != correct:
            cpt = 0
            print('Incorrect. The expected answer is ' + str(correct))
        else:
            cpt += 1
            print("Correct! You've gotten " + str(cpt) + " correct in a row.")

    print('Congratulations! You mastered addition.')
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
