import random, string, sys, textwrap, time

import standard_commands

print """
Game Rules:
When the game starts, your terminal window will begin to fill with characters.
Hidden in the random characters are actual words that make up a code phrase.
Find the code phrase, and enter it into the command prompt to hack into the
mainframe. The command prompt will appear again after the program has finished
running. You will have 20 seconds to enter the phrase, otherwise the alarm
will sound and the FBI will be sent to your door. Type 'begin' to start the
program.
"""

class DataBreachCmd(standard_commands.StandardCommands):
	prompt = '\n> '


	def __init__(self, words):
		standard_commands.StandardCommands.__init__(self)
		self.words = words


	def default(self, arg):
		print arg
		if arg == self.words:
			print "Congrats. You're in the mainframe!"
		else:
			super(DataBreachCmd, self).default()


	def do_greet(self, arg):
		"""Exits the program."""
		print "Hey!"


	def do_begin(self, arg):
		"""Starts the program."""
		DataBreach(self.words)


class DataBreach(object):

	def __init__(self, phrase):
		self.sleep_time = .08
		self.phrase = phrase
		self.start()

	def start(self, looping = True):
		characters = string.ascii_letters + string.digits + string.punctuation
		while looping:
			time.sleep(self.sleep_time)
			random_int = random.randrange(100)
			if random_int >= 99:
				self.show_word(self.phrase)
			else:
				character = random.choice(characters)
				print character,
				sys.stdout.flush()

	def show_word(self, word):
		counter = 0
		for letter in word:
			time.sleep(self.sleep_time)
			print word[counter],
			sys.stdout.flush()
			counter += 1


DataBreachCmd("Test").cmdloop()
