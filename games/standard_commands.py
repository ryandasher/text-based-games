import cmd

class StandardCommands(cmd.Cmd):
	prompt = '\n> '


	def __init__(self):
		cmd.Cmd.__init__(self)


    # The default() method is called when none of the other do_*() command
    # methods match.
	def default(self, arg):
		"""Called when none of the other do_*() command methods match."""
		print("'%s' is not a valid command. "
			  "Type 'help' for a list of commands." % (arg))


	def do_exit(self, arg):
		"""Exits the program."""
		return True


	def do_quit(self, arg):
		"""Exits the program."""
		return True
