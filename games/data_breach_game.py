from threading import Thread
from time import sleep

import json, random, string, sys, time

import standard_commands

SECONDS = 30

print """
Game Rules:
When the game starts, your terminal window will begin to fill with characters.
Hidden in the random characters are words that make up the password to access
the mainframe. Find all of the words, and enter them into the command prompt
when the output stops. Leave a single space between each word, do not enter any
commas. You will have %s seconds to enter the words, otherwise the alarm will
sound and suspicious men will be sent to your door. See the
data_breach_word_list.json file if you want to peek at the words that might
show up in the program. Type 'begin' to start the program.
""" % SECONDS

class DataBreachCmd(standard_commands.StandardCommands):
	"""Commands specific to the the Data Breach Game."""
	def __init__(self):
		standard_commands.StandardCommands.__init__(self)
		self.game = DataBreach()
		self.passphrase = self.game.create_passphrase()
		self.program_started = False


	def default(self, arg):
		"""
		Catches any inputs that do not match an existing method. Compares
		against the generated passphrase.
		"""
		if arg == self.passphrase and not self.game.counted_down:
			print "Congrats. You're in the mainframe!"
			return True
		elif self.game.counted_down:
			print "Your time ran out and you've been logged off. Try again!"
			return True
		else:
			standard_commands.StandardCommands.default(self, arg)


	def do_begin(self, arg):
		"""Starts the program."""
		if not self.program_started:
			self.game.start_game()
			self.program_started = True
		else:
			print "You've already run the program."


	do_start = do_begin


class DataBreach(object):
	"""Data Breach Game Class that controls all game logic."""
	def __init__(self):
		self.sleep_time = .03
		self.word_list = self.load_word_list()
		self.counted_down = False


	def load_word_list(self):
		"""
		Load the word list JSON file, and randomly select five words for our
		passphrase using a list comprehension.
		"""
		with open('data/data_breach_word_list.json') as json_file:
			words = json.load(json_file)
		# Return a list of randomly selected words. Words can be repeated.
		return [words[random.randint(0, 58)] for i in range(5)]


	def create_passphrase(self):
		"""Join our random list of words into a single spaced string."""
		return ' '.join(self.word_list)


	def start_game(self):
		"""Call the methods associated with running game logic."""
		self.output_characters()
		countdown = Thread(target = self.countdown, args = (SECONDS,))
		countdown.daemon = True
		print "\n\nYou have %s seconds to solve the puzzle." % SECONDS
		countdown.start()


	def output_characters(self):
		"""
		Output random junk characters mixed with the words that make up the
		passphrase. Terminate the output when all words from the list have been
		displayed.
		"""
		characters = string.ascii_letters + string.digits + string.punctuation
		# Indicate that the program has terminated.
		self.word_list.append('...terminate')
		while len(self.word_list):
			time.sleep(self.sleep_time)
			if random.randrange(1000) >= 995:
				self.show_word(self.word_list[0])
				self.word_list.pop(0)
			else:
				character = random.choice(characters)
				print character,
				sys.stdout.flush()


	def show_word(self, word):
		"""
		Display one of the words from the passphrase.

		Args:
		word -- Passphrase part to display (string).
		"""
		for letter in word:
			print letter,
			sys.stdout.flush()
			time.sleep(self.sleep_time)


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


DataBreachCmd().cmdloop()
