from threading import Thread
from time import sleep

import sys

import standard_commands

class BombDefusalCmd(standard_commands.StandardCommands):
    """Commands specific to the Bomb Defusal Game."""
    def __init__(self):
        standard_commands.StandardCommands.__init__(self)
        self.game = BombDefusal()
        self.game.start_countdown()
        self.countdown_message = "The timer ran out. You've been incinerated."


    def do_cut(self, arg):
        """Cut a wire."""
        self.game.cut_wire(arg)
        if self.game.counted_down:
            print self.countdown_message
            return True
        else:
            print self.game.wires[arg]
        if any(color in self.game.cut_wires for color in ('red', 'green')):
            return True


    def default(self, arg):
        if self.game.counted_down:
            print self.countdown_message
            return True
        else:
            standard_commands.StandardCommands.default(self, arg)


class BombDefusal(object):
    """Bomb Defusal game class that controls all the game logic."""
    def __init__(self):
        self.counted_down = False
        self.wires = {
            'green': 'The bomb has been deactivated.',
            'yellow': 'Nothing happens.',
            'red': 'The bomb explodes. You have been incinerated.'
        }
        self.cut_wires = []


    def start_countdown(self):
        """Call the methods associated with running game logic."""
        countdown = Thread(target = self.countdown, args = (5,))
        countdown.daemon = True
        countdown.start()


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


    def cut_wire(self, color):
        """
        Cut one of the wires.

        Args:
        color -- The color of the wire you intend to cut (string).
        """
        if color in self.cut_wires:
            print "You've already cut this wire!"
        else:
            self.cut_wires.append(color)


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
        sleep(.2)


introduction = [
    "There is a bomb sitting in front of you...\n",
    "It will detonate in five seconds."
]

print_characters(introduction)
BombDefusalCmd().cmdloop()
