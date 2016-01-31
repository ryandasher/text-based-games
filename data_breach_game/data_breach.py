import cmd, textwrap, random, string, sys, time

from threading import Thread

print "Your pudgy fingers sidle up to the keys on the keyboard."

def output_jargon(looping = True):
	characters = string.ascii_letters + string.digits + string.punctuation
	while looping:
		time.sleep(.02)
		character = random.choice(characters)
		print character,
		sys.stdout.flush()


class DataBreachCmd(cmd.Cmd):
	prompt = '\n> '

	def default(self, arg):
		print '%s is not a valid command. Type "help" for a list of commands.'


output_jargon()
# hacking_display = Thread(target = output_jargon)
# hacking_display.daemon = True
# hacking_display.start()
# DataBreachCmd().cmdloop()
