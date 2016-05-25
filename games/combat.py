from threading import Thread

import json, sys

import standard_commands

class CombatCmd(standard_commands.StandardCommands):
	"""Commands specific to the Combat game."""
	def __init__(self, enemy):
		standard_commands.StandardCommands.__init__(self)
		self.game = CombatGame(enemy)
		self.program_started = False
		self.player_turn = False


	def default(self, arg):
		pass


	def do_fight(self, arg):
		"""Start the fight."""
		if not self.program_started:
			self.game.start_fight()
			self.program_started = True
		else:
			print "You're already in a fight!"


	def do_turn(self, arg):
		pass


class CombatGame(object):
	"""Initiate combat with an enemy character."""
	def __init__(self, enemy):
		self.enemy = enemy
		self.player_health, self.enemy_health = 2
		with open('data/combat_moves.json') as moves_file:
			self.move_set = json.load(moves_file)


	def start_fight(self):
		pass


	def determine_countdown(self):
		pass


	def determine_defensive_action(self):
		pass


	def determine_offensive_action(self):
		pass


	def decrement_health(self, character):
		if character == player:
			self.player_health -= 1
		else:
			self.enemy_health -= 1

