from threading import Thread
from time import sleep

import json, sys

import standard_commands

STORY = open("data/bomb_defusal.json", "r")
PARSED_JSON = json.loads(STORY)

class BombDefusalCmd(standard_commands.StandardCommands):
    """Commands specific to the Bomb Defusal Game."""
    def __init__(self):
        self.game = BombDefusal()


    def do_green(self, arg):
        """Cut a wire."""
        self.game.cut_wire(arg)


    def do_answer(self, arg):
        """Answer the phone."""
        pass


    do_red = do_green
    do_yellow = do_green
    do_phone = do_answer


class BombDefusal(object):
    """Bomb Defusal game class that controls all the game logic."""
    def __init__(self):
        self.counted_down = False
        self.green_wire, self.yellow_wire, self.red_wire = "Intact"


    def countdown(self, seconds):
        """
        Run a countdown.

        Args:
        seconds -- Amount of seconds to countdown (integer).
        """
        while seconds:
            seconds -= 1
            sleep(1)
        self.counted_down = True


    def timer_beeps(self, amount):
        """
        Let's show some incremental beeps to increase the tension.

        Args:
        amount -- How many beeps we want to display (integer).
        """
        while amount > 0:
            print "(Beep)...\n"
            amount -= 1
            sleep(1)


    def cut_wire(self, color):
        """
        Cut one of the wires.

        Args:
        color -- The color of the wire you intend to cut (string).
        """
        pass


def print_characters(characters):
    """
    Slowly print characters, so users aren't inundated with a large block of
    text at one time.

    Args:
    characters -- The characters to print (string).
    """
    for character in characters:
        print character,
        sys.stdout.flush()
        time.sleep(.05)


def choices(color):
    """
    This function contains all the conditional logic when making choices.
    I know this is one giant gross conditional. I will think of better ways
    to do this in the future.
    """
    if color.lower() == 'green':
        line_number = 8
        while line_number < 12:
            print story_lines[line_number]
            line_number += 1
        # TODO: We need a way to stop the initial countdown
        short_countdown = Thread(target = total_countdown, args = (60,))
        short_countdown.daemon = True
        short_countdown.start()
        second_choice = raw_input("Choose a colored wire to cut, or do something else...\n>")
        print "\n"
        if second_choice.lower() == 'yellow':
            print story_lines[17]
            phone_choice = raw_input("Do you answer the phone?\n>")
            print "\n"
            if 'y' in phone_choice.lower():
                print story_lines[25]
                close_it_up()
            else:
                print story_lines[23]
                close_it_up()
        elif second_choice.lower() == 'red':
            story_lines[19]
            close_it_up()
        else:
            print "As you attempt to %s, your phone rings." % second_choice
            phone_choice = raw_input("Do you answer the phone?\n>")
            print "\n"
            if 'y' in phone_choice.lower():
                print story_lines[25]
                close_it_up()
            else:
                print story_lines[23]
                close_it_up()
    elif color.lower() == 'yellow':
        print story_lines[13]
        second_choice = raw_input("Choose another wire to cut...\n>")
        print "\n"
        if second_choice.lower() == 'green':
            line_number = 8
            while line_number < 12:
                print story_lines[line_number]
                line_number += 1
            # TODO: We need a way to stop the initial countdown
            short_countdown = Thread(target = total_countdown, args = (60,))
            short_countdown.daemon = True
            short_countdown.start()
            tertiary_choice = raw_input("Cut the red wire, or do something else...\n>")
            print "\n"
            if tertiary_choice.lower() == 'red':
                print story_lines[19]
                close_it_up()
            else:
                print "As you attempt to %s, your phone rings." % second_choice
                phone_choice = raw_input("Do you answer the phone?\n>")
                print "\n"
                if 'y' in phone_choice.lower():
                    print story_lines[25]
                    close_it_up()
                else:
                    print story_lines[23]
                    close_it_up()
        elif second_choice.lower() == 'red':
            print story_lines[19]
            close_it_up()
        else:
            print story_lines[21]
            color_choice = raw_input("What color wire will you cut?\n>")
            print "\n"
            if color_choice.lower() == 'yellow':
                print "Your incompetence causes your partner to push you aside and handle the task without your help."
                close_it_up()
            else:
                choices(color_choice)
    elif color.lower() == 'red':
        print story_lines[15]
        close_it_up()
    else:
        print story_lines[21]
        color_choice = raw_input("What color wire will you cut?\n> ")
        print "\n"
        choices(color_choice)


print story_lines[0]
sleep(3)
timer_beeps(3)
n = 1
while n < 6:
    print story_lines[n]
    n += 1
    enter = raw_input("(continue)\n")

countdown = Thread(target = total_countdown, args = (277,))
# Set the thread to a daemon thread, so it dies when we exit the file.
countdown.daemon = True
countdown.start()

color_choice = raw_input("What color wire will you cut?\n> ")
print "\n"
choices(color_choice)