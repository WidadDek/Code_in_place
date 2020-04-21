from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.

 if( beepers_present()): #even
        return_to_wall()
        upside_down()
        while front_is_clear():
            put_beeper()
            move()
            if front_is_clear():
                move()

"""

def main():
    if front_is_clear():
        put_beepers()
        upside_down()

        while front_is_clear(): move()
        pick_beeper()
        upside_down()
        move()
        pick_beepers()

    else:
        put_beeper()

def put_beepers():
    while front_is_clear():
        put_beeper()
        move()

def pick_beepers():
    while beepers_present(): move()

    upside_down()
    if front_is_clear(): move()

    if(beepers_present()):
        pick_beeper()
        move()
        pick_beepers()
    else:
        put_beeper()

def upside_down():
    for i in range(2):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()
