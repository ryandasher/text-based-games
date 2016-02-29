import json, random, string, sys, textwrap, time

import standard_commands

SECONDS = 30

print """
Game Rules:
When the game starts, your terminal window will begin to fill with characters.
Hidden in the random characters are words that make up the password to access
the mainframe. Find all of the words, and enter them into the command prompt
when the output stops. Leave a single space between each word, do not enter any
commas. You will have %s seconds to enter the words, otherwise the alarm will
sound and the FBI will be sent to your door. Type 'begin' to start the program.
""" % (SECONDS)

# TODO: Add documentation comments.
class DataBreachCmd(standard_commands.StandardCommands):
	prompt = '\n> '


	def __init__(self):
		standard_commands.StandardCommands.__init__(self)
		self.game = DataBreach()
		self.passphrase = self.game.create_passphrase()


	def default(self, arg):
		if arg == self.passphrase:
			print "Congrats. You're in the mainframe!"
			return True
		else:
			standard_commands.StandardCommands.default(self, arg)


	def do_begin(self, arg):
		"""Starts the program."""
		self.game.output_characters()


# TODO: Add documentation comments.
class DataBreach(object):

	def __init__(self):
		self.sleep_time = .03
		self.word_list = self.load_word_list()


	def load_word_list(self):
		with open('data/data_breach_word_list.json') as json_file:
			words = json.load(json_file)
		# Return a list of randomly selected words. Words can be repeated.
		return [words[random.randint(0, 58)] for i in range(5)]


	def create_passphrase(self):
		return ' '.join(self.word_list)


	def output_characters(self):
		characters = string.ascii_letters + string.digits + string.punctuation
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
		counter = 0
		for letter in word:
			print word[counter],
			sys.stdout.flush()
			time.sleep(self.sleep_time)
			counter += 1


DataBreachCmd().cmdloop()