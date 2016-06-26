from threading import Thread

import json, random, sys

import standard_commands

print """
Welcome to Combat! Type in the word 'fight' to begin the fight of your life!
You will be shown an action or defense message that you will need to retype
in a set amount of time. If you complete the sentence before the countdown
expires, then you will successfully defend yourself/hit your enemy!
"""

class CombatCmd(standard_commands.StandardCommands):
    """Commands specific to the Combat game."""
    def __init__(self, enemy):
        standard_commands.StandardCommands.__init__(self)
        self.game = CombatGame(enemy)
        self.enemy = enemy
        self.program_started = False
        self.action_message = None
        self.attacker = None


    def default(self, arg):
        if arg == self.action_message:
            if self.attacker != self.enemy:
                self.game.decrement_hp(self.enemy)
            print "PASS!"
        elif self.program_started:
            self.game.decrement_hp('player')
            print "FAIL!"
        else:
            standard_commands.StandardCommands.default(self, arg)
            return

        if self.game.enemy_hp == 0:
            print "You defeated your enemy! Type 'fight' to begin a new game!"
            self.program_started = False
            self.action_message, self.attacker = None, None
        elif self.game.player_hp == 0:
            print "You lost the fight! Type 'fight' to begin a new game!"
            self.program_started = False
            self.action_message, self.attacker = None, None

        if self.program_started:
            self.action_message, self.attacker = self.game.show_action()
            print self.action_message


    def do_fight(self, arg):
        """Initiate the fight."""
        if not self.program_started:
            self.program_started = True
            self.action_message, self.attacker = self.game.show_action()
            print self.action_message
        else:
            print "You're already in a fight!"


    def do_turn(self, arg):
        pass


class CombatGame(object):
    """Initiate combat with an enemy character."""
    def __init__(self, enemy):
        self.enemy = enemy
        self.player_hp, self.enemy_hp = (2, 2)
        with open('data/combat_moves.json') as moves_file:
            self.move_set = json.load(moves_file)


    def show_action(self):
        attacker = random.choice([self.enemy, "player"])

        if attacker == self.enemy:
            print "You are on defense!\n"
            msg = self.determine_action_msg('defense')
        else:
            print "You're on the attack!\n"
            msg = self.determine_action_msg('offense')

        return msg, attacker


    def determine_action_msg(self, action):
        action = random.choice(self.move_set[0][action])
        movement = random.choice(self.move_set[0]['movements'])
        direction_1 = random.choice(self.move_set[0]['directions'])
        direction_2 = random.choice(self.move_set[0]['directions'])
        return movement + ' ' + direction_1 + ' and ' + action + ' ' + direction_2


    def determine_countdown(self):
        pass


    def decrement_hp(self, character):
        if character == self.enemy:
            self.enemy_hp -= 1
        else:
            self.player_hp -= 1


CombatCmd("Orc").cmdloop()
