# Text Games

This is my repository for some simple text-based games I'm creating. Hopefully they will get better over time.

You can run the text game by going into your command prompt, and running the equivalent of:

$ python games/filename.py

## Bomb Defusal

My first text game. It's vague and not very good. You're tasked with defusing a bomb in a train terminal, and man there is a lot of branching in that choices function. And also apparently I didn't know how to leverage JSON back then.

#### TODOS:

* Refactor this code.
* Write tests.
* Move the text data to a JSON file.

## Data Breach

Find words amid random junk characters and enter them into a command prompt to "hack into the mainframe".

#### TODOS:

* Fix countdown logic so program exits without user input.
* Make difficulty levels (randomize the casing of words, lower timer threshold, use longer passphrases).
* Write tests.
* Sometimes real words show up in the jargon. What can be done about this?

## Tutorial Game

A text game tutorial by Al Sweigart, which I learned plenty from.

#### TODOS:

* Refactor this code (Make it DRYer, rename variables, etc.).
