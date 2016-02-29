# Text Games

This is my repository for some simple text-based games I'm creating. Hopefully they will get better over time.

You can run the text game by going into your command prompt, and running the equivalent of:

$ python games/filename.py

## Bomb Defusal

My first text game. It's vague and not very good. You're tasked with defusing a bomb in a train terminal, and man there is a lot of branching in that choices function. And also apparently I didn't know how to leverage JSON back then.

## TODOS:

Refactor this code.
Write tests.
Move the text data to a JSON file.

## Data Breach

Find words amid random junk characters and enter them into a command prompt to "hack into the mainframe".

### TODOS:

Write logic that will start a countdown to run concurrent with the user input after the game has completed.
Make difficulty levels (randomize the casing of words, lower timer threshold, use longer passphrases).
Write tests.
Write class and method documentation.
Final word in the passphrase always appears at the end of the character output.
See if there is a way to wrap the character output after 80 characters.

## Tutorial Game

A text game tutorial by Al Sweigart, which I learned plenty from.

### TODOS:

Refactor this code (Make it DRYer, rename variables, etc.).
