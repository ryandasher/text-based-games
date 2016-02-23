from time import sleep
from threading import Thread

story = open("data/bomb_defusal.txt", "r")
story_lines = story.readlines()

"""
With this simple game, I experimented with housing the story text in a separate
text file. It's nice not having all of the story text inside the python file,
but keeping track of the line numbers in variables isn't ideal.
"""

def timer_beeps(amount):
    """
    Let's show some incremental beeps to ratchet up the tension.
    """
    while amount > 0:
        print "(Beep)..."
        print "\n"
        amount -= 1
        sleep(1)


def total_countdown(seconds):
    """
    This function will begin counting down the total time once it's displayed 
    to the user.
    """
    while seconds:
        seconds -= 1
        sleep(1)
    if seconds == 0:
        print story_lines[19]
        close_it_up()


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


def close_it_up():
    """
    A simple function to help us wrap everything up.
    """
    story.close()
    exit(1)


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