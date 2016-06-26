from threading import Thread

import json, random, sys

import standard_commands

print """
Welcome to Combat! Type in the word 'fight' to begin a fight for your life!
You will be shown an offensive or defensive message that you will need to retype
in a set amount of time. If you complete the sentence before the countdown
expires, then you will successfully defend yourself/hit your enemy!
"""

class CombatCmd(standard_commands.StandardCommands):
    """Commands specific to the Combat game."""
    def __init__(self, enemy):
        standard_commands.StandardCommands.__init__(self)
        self.game = CombatGame(enemy)


    def default(self, arg):
        if arg == self.game.msg:
            self.game.check_action_result(True)
        elif self.game.fight_started:
            self.game.check_action_result(False)
        else:
            standard_commands.StandardCommands.default(self, arg)
            return

        if self.game.enemy_hp == 0 or self.game.player_hp == 0:
            print "The fight is over! Type 'fight' to begin a new game!"
            self.game.reset_game_state()

        if self.game.fight_started:
            self.game.show_action()
            print self.game.msg


    def do_fight(self, arg):
        """Initiate the fight."""
        if not self.game.fight_started:
            self.game.show_action()
            print self.game.msg
        else:
            self.game.check_action_result(False)
            if self.game.player_hp == 0:
                print "The fight is over! Type 'fight' to begin a new game!"
                self.game.reset_game_state()


class CombatGame(object):
    """Initiate combat with an enemy character."""
    def __init__(self, enemy):
        self.enemy = enemy
        with open('data/combat_moves.json') as moves_file:
            self.move_set = json.load(moves_file)
        self.reset_game_state()


    def show_action(self):
        if self.fight_started == False: self.fight_started = True

        self.attacker = random.choice([self.enemy, "player"])

        if self.attacker == self.enemy:
            print "You are on defense!\n"
            self.msg = self.determine_action_msg('defense')
        else:
            print "You're on the attack!\n"
            self.msg = self.determine_action_msg('offense')


    def determine_action_msg(self, action):
        action = random.choice(self.move_set[0][action])
        movement = random.choice(self.move_set[0]['movements'])
        direction_1 = random.choice(self.move_set[0]['directions'])
        direction_2 = random.choice(self.move_set[0]['directions'])
        return movement + ' ' + direction_1 + ' and ' + action + ' ' + direction_2


    def determine_countdown(self):
        pass


    def check_action_result(self, action_success):
        if action_success == True:
            if self.attacker != self.enemy:
                self.decrement_hp(self.enemy)
            else:
                print "You successfully defended yourself!"
        else:
            if self.attacker == self.enemy:
                self.decrement_hp('player')
            else:
                print "You failed to connect on your blow!"


    def decrement_hp(self, character):
        if character == self.enemy:
            print "You successfully hit the %s!" % self.enemy
            self.enemy_hp -= 1
        else:
            print "The %s has hit you!" % self.enemy
            self.player_hp -= 1


    def reset_game_state(self):
        self.fight_started = False
        self.player_hp, self.enemy_hp = (2, 2)
        self.attacker, self.msg = (None, None)


CombatCmd("Orc").cmdloop()
