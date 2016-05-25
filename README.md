# Text Games

This is my repository for some simple text-based games I'm creating. Hopefully they will get better over time.

You can run the text game by going into your command prompt, and running the equivalent of:

$ python games/filename.py

## Bomb Defusal

My first attempt at a text game. It has been significantly refactored at this point, as the small narrative has been removed.

#### TODOs:

* Add difficulty levels.
* Add much needed complexity.
* Write tests.

## Data Breach

Find words amid random junk characters and enter them into a command prompt to "hack into the mainframe".

#### TODOs:

* Fix countdown logic so program exits without user input.
* Make difficulty levels (randomize the casing of words, lower timer threshold, use longer passphrases).
* Write tests.
* Sometimes real words show up in the jargon. What can be done about this?

## Tutorial Game

A text game tutorial by Al Sweigart, which I learned plenty from.

#### TODOs:

* Refactor this code (Make it DRYer, rename variables, etc.).

## Combat Game

Retype the action prompts within the time limit to successfully defend your character/attack the enemy in medieval combat.

#### TODOs:

* Add difficulty levels -- Randomly generate a different enemy based on difficulty.
* Create enemies with different statistics and weapons.
* Write tests.
