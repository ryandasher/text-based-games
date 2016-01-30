#!/usr/bin/python

"""
Text game tutorial by Al Sweigart:
https://github.com/asweigart/textadventuredemo

This demo purposely avoids using classes and object-oriented programming
concepts in order to make the process easier to understand for new programmers.
"""

"""
These constant variables are used because if I mistype them, Python will
immediately throw up an error message since no variable with the typo
name will exist. If we mistyped the strings, the bugs that it produces
would be harder to find.
"""
DESC = 'desc'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
UP = 'up'
DOWN = 'down'
GROUND = 'ground'
SHOP = 'shop'
GROUNDDESC = 'grounddesc'
SHORTDESC = 'shortdesc'
LONGDESC = 'longdesc'
TAKEABLE = 'takeable'
EDIBLE = 'edible'
DESCWORDS = 'descwords'

SCREEN_WIDTH = 80

"""
The game world data is stored in a dictionary (which itself has dictionaries
and lists). Python's normal rules of indentation are suspended when typing out
a dictionary value until it encounters the closing curly brace, which is
helpful for us to make the dictionary value readable.

Each dictionary value inside the world variable is a different area in the
game world. The key is a string (i.e. 'Town Square') that is the reference
name of the location. It will also be displayed as the title of the area.

The value is another dictionary, which has keys 'desc', 'north', 'south',
'east', 'west', 'up', 'down', 'shop', and 'ground'. We use the constant
variables (e.g. DESC, NORTH, etc.) instead of strings in case we make
typos.

DESC is a text description of the area. SHOP, if it exists, is a list of
items that can be bought at this area. (We don't implement money in this
program, so everything is free.) GROUND is a list of items that are on
the ground in this area. The directions (NORTH, SOUTH, UP, etc.) are the
areas that exist in that direction.
"""
world_rooms = {
    'Town Square': {
        DESC: 'The town square is a large open space with a fountain in the center. Streets lead in all directions.',
        NORTH: 'North Y Street',
        EAST: 'East X Street',
        SOUTH: 'South Y Street',
        WEST: 'West X Street',
        GROUND: ['Welcome Sign', 'Fountain']},
    'North Y Street': {
        DESC: 'The northern end of Y Street has really gone down hill. Pot holes are everywhere, as are stray cats, rats, and wombats.',
        WEST: 'Thief Guild',
        EAST: 'Bakery',
        SOUTH: 'Town Square',
        GROUND: ['Do Not Take Sign Sign']},
    'Thief Guild': {
        DESC: 'The Thief Guild is a dark den of unprincipled types. You clutch your purse (though several other people here would like to clutch your purse as well).',
        SOUTH: 'West X Street',
        EAST: 'North Y Street',
        GROUND: ['Lock Picks', 'Silly Glasses']},
    'Bakery': {
        DESC: 'The delightful smell of meat pies fills the air, making you hungry. The baker flashes a grin, as he slides a box marked "Not Human Organs" under a table with his foot.',
        WEST: 'North Y Street',
        SOUTH: 'East X Street',
        SHOP: ['Meat Pie', 'Donut', 'Bagel'],
        GROUND: ['Shop Howto']},
    'West X Street': {
        DESC: 'West X Street is the rich section of town. So rich, they paved the streets with gold. This probably was not a good idea. The thief guild opened up the next day.',
        NORTH: 'Thief Guild',
        EAST: 'Town Square',
        SOUTH: 'Blacksmith',
        WEST: 'Used Anvils Store',
        GROUND: []},
    'Used Anvils Store': {
        DESC: 'The anvil store has anvils of all types and sizes, each previously-owned but still in servicable condition. However, due to a bug in the way this game is designed, you can buy anvils like any other item and walk around, but if you drop them they cannot be picked up since their TAKEABLE value is set to False. The code should be changed so that it\'s not possible for shops to sell items with TAKEABLE set to False.',
        EAST: 'West X Street',
        SHOP: ['Anvil'],
        GROUND: ['Anvil', 'Anvil', 'Anvil', 'Anvil']},
    'East X Street': {
        DESC: 'East X Street. It\'s like X Street, except East.',
        NORTH: 'Bakery',
        WEST: 'Town Square',
        SOUTH: 'Wizard Tower',
        GROUND: []},
    'Blacksmith': {
        DESC: 'The blacksmith loudly hammers a new sword over her anvil. Swords, axes, butter knives all line the walls of her workshop, available for a price.',
        NORTH: 'West X Street',
        EAST: 'South Y Street',
        SHOP: ['Sword', 'War Axe', 'Chainmail T-Shirt'],
        GROUND: ['Anvil', 'Shop Howto']},
    'South Y Street': {
        DESC: 'The Christmas Carolers of South Y Street are famous for all legally changing their name to Carol. They are also famous for singing year-round, in heavy fur coats and wool mittens, even in the summer. That\'s dedication to their craft!',
        NORTH: 'Town Square',
        WEST: 'Blacksmith',
        GROUND: []},
    'Wizard Tower': {
        DESC: 'Zanny magical antics are afoot in the world-famous Wizard Tower. Cauldrons bubble, rats talk, and books float midair in this center of magical discovery.',
        NORTH: 'East X Street',
        UP: 'Observation Deck',
        GROUND: ['Crystal Ball', 'Floating Book', 'Floating Book']},
    'Observation Deck': {
        DESC: 'You can see the entire town from the top of the Wizard Tower. Everybody looks like ants, especially the people transformed into ants by the wizards of the tower!',
        DOWN: 'Wizard Tower',
        UP: 'Magical Escalator to Nowhere',
        GROUND: ['Telescope']},
    'Magical Escalator to Nowhere': {
        DESC: 'No matter how much you climb the escalator, it doesn\'t seem to be getting you anywhere.',
        UP: 'Magical Escalator to Nowhere',
        DOWN: 'Observation Deck',
        GROUND: []},
    }

"""
This is the index of all possible items in the game world. Note that These
key-value pairs are more like blueprints than actual items. The actual
items exist in the GROUND value in an area's entry in the world variable.

The GROUNDDESC value is a short string that displays in the area's description.
The SHORTDESC value is a short string that will be used in sentences like, "You
drop X." or "You buy X."
The LONGDESC value is displayed when the player looks at the item.
The TAKEABLE Boolean value is True if the player can pick up the item and put
it in their inventory.
The DESCWORDS value is a list of strings that can be used in the player's
commands. For example, if this is ['welcome', 'sign'] then the player can type
a command such as "take sign" or "look welcome".
The TAKEABLE value is True if the item can be picked up off the ground. If
this key doesn't exist, it defaults to True.
The EDIBLE value is True if the item can be eaten. If this key doesn't exist,
it defaults to False.
"""
world_items = {
    'Welcome Sign': {
        GROUNDDESC: 'A welcome sign stands here.',
        SHORTDESC: 'a welcome sign',
        LONGDESC: 'The welcome sign reads, "Welcome to this text adventure demo. You can type "help" for a list of commands to use. Be sure to check out Al\'s cool programming books at http://inventwithpython.com"',
        TAKEABLE: False,
        DESCWORDS: ['welcome', 'sign']},
    'Do Not Take Sign Sign': {
        GROUNDDESC: 'A sign stands here, not bolted to the ground.',
        SHORTDESC: 'a sign',
        LONGDESC: 'The sign reads, "Do Not Take This Sign"',
        DESCWORDS: ['sign']},
    'Fountain': {
        GROUNDDESC: 'A bubbling fountain of green water.',
        SHORTDESC: 'a fountain',
        LONGDESC: 'The water in the fountain is a bright green color. Is that... gatorade?',
        TAKEABLE: False,
        DESCWORDS: ['fountain']},
    'Sword': {
        GROUNDDESC: 'A sword lies on the ground.',
        SHORTDESC: 'a sword',
        LONGDESC: 'A longsword, engraved with the word, "Exkaleber"',
        DESCWORDS: ['sword', 'exkaleber', 'longsword']},
    'War Axe': {
        GROUNDDESC: 'A mighty war axe lies on the ground.',
        SHORTDESC: 'a war axe',
        LONGDESC: 'The mighty war axe is made with antimony impurities from a fallen star, rendering it surpassingly brittle.',
        DESCWORDS: ['axe', 'war', 'mighty']},
    'Chainmail T-Shirt': {
        GROUNDDESC: 'A chainmail t-shirt lies wadded up on the ground.',
        SHORTDESC: 'a chainmail t-shirt',
        LONGDESC: 'The chainmail t-shirt has a slogan and arrow engraved on the front: "I\'m with Stupid"',
        DESCWORDS: ['chainmail', 'chain', 'mail', 't-shirt', 'tshirt', 'stupid']},
    'Anvil': {
        GROUNDDESC: 'The blacksmith\'s anvil, far too heavy to pick up, rests in the corner.',
        SHORTDESC: 'an anvil',
        LONGDESC: 'The black anvil has the word "ACME" engraved on the side.',
        TAKEABLE: False,
        DESCWORDS: ['anvil']},
    'Lock Picks': {
        GROUNDDESC: 'A set of lock picks lies on the ground.',
        SHORTDESC: 'a set of lock picks',
        LONGDESC: 'A set of fine picks for picking locks.',
        DESCWORDS: ['lockpicks', 'picks', 'set']},
    'Silly Glasses': {
        GROUNDDESC: 'A pair of those silly gag glasses with the nose and fake mustache rest on the ground.',
        SHORTDESC: 'a pair of silly fake mustache glasses',
        LONGDESC: 'These glasses have a fake nose and mustache attached to them. The perfect disguise!',
        DESCWORDS: ['glasses', 'silly', 'fake', 'mustache']},
    'Meat Pie': {
        GROUNDDESC: 'A suspicious meat pie rests on the ground.',
        SHORTDESC: 'a meat pie',
        LONGDESC: 'A meat pie. It tastes like chicken.',
        EDIBLE: True,
        DESCWORDS: ['pie', 'meat']},
    'Bagel': {
        GROUNDDESC: 'A bagel rests on the ground. (Gross.)',
        SHORTDESC: 'a bagel',
        LONGDESC: 'It is a donut-shaped bagel.',
        EDIBLE: True,
        DESCWORDS: ['bagel']},
    'Donut': {
        GROUNDDESC: 'A donut rests on the ground. (Gross.)',
        SHORTDESC: 'a donut',
        LONGDESC: 'It is a bagel-shaped donut.',
        EDIBLE: True,
        DESCWORDS: ['donut']},
    'Crystal Ball': {
        GROUNDDESC: 'A glowing crystal ball rests on a small pillow.',
        SHORTDESC: 'a crystal ball',
        LONGDESC: 'The crystal ball swirls with mystical energy, forming the words "Answer Unclear. Check Again Later."',
        DESCWORDS: ['crystal', 'ball']},
    'Floating Book': {
        GROUNDDESC: 'A magical book floats here.',
        SHORTDESC: 'a floating book',
        LONGDESC: 'This magical tomb doesn\'t have a lot of pictures in it. Boring!',
        DESCWORDS: ['book', 'floating']},
    'Telescope': {
        GROUNDDESC: 'A telescope is bolted to the ground.',
        SHORTDESC: 'a telescope',
        LONGDESC: 'Using the telescope, you can see your house from here!',
        TAKEABLE: False,
        DESCWORDS: ['telescope']},
    'README Note': {
        GROUNDDESC: 'A note titled "README" rests on the ground.',
        SHORTDESC: 'a README note',
        LONGDESC: 'The README note reads, "Welcome to the text adventure demo. Be sure to check out the source code to see how this game is put together."',
        EDIBLE: True,
        DESCWORDS: ['readme', 'note']},
    'Shop Howto': {
        GROUNDDESC: 'A "Shopping HOWTO" note rests on the ground.',
        SHORTDESC: 'a shopping howto',
        LONGDESC: 'The note reads, "When you are at a shop, you can type "list" to show what is for sale. "buy <item>" will add it to your inventory, or you can sell an item in your inventory with "sell <item>". (Currently, money is not implemented in this program.)',
        EDIBLE: True,
        DESCWORDS: ['howto', 'note', 'shop']},
    }

import cmd, sys, textwrap

location = 'Town Square' # Start in town square.
inventory = ['README Note', 'Sword', 'Donut'] # Start with basic inventory.
show_full_exits = True

def display_location(loc):
    """A helper function for displaying an area's description and exits"""
    # Print a room name.
    print(loc)
    # print('=' + len(loc))

    # Print the room's description (using textwrap.wrap()).
    print('\n'.join(textwrap.wrap(world_rooms[loc][DESC], SCREEN_WIDTH)))

    # Print all the items on the ground.
    if len(world_rooms[loc][GROUND]) > 0:
        print "\n"
        for item in world_rooms[loc][GROUND]:
            print(world_items[item][GROUNDDESC])

    # Print all the exits.
    exits = []
    for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
        if direction in world_rooms[loc].keys():
            exits.append(direction.title())

    print "\n"
    if show_full_exits:
        for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
            if direction in world_rooms[location]:
                print('%s: %s' % (direction.title(),
                                  world_rooms[location][direction]))
    else:
        print('Exits: %s' % ' '.join(exits))


def get_all_desc_words(item_list):
    """
    Returns a list of 'description words' for each item named in item_list.
    """
    item_list = list(set(item_list)) # Make item_list unique.
    desc_words = []
    for item in item_list:
        desc_words.extend(world_items[item][DESCWORDS])
    return list(set(desc_words))


def get_all_first_desc_words(item_list):
    """
    Returns a list of the first 'description word' in the list of description
    words for each item named in item_list.
    """
    item_list = list(set(item_list)) # Make item_list unique.
    desc_words = []
    for item in item_list:
        desc_words.append(world_items[item][DESCWORDS][0])
    return list(set(desc_words))


def get_all_items_matching_desc(desc, item_list):
    item_list = list(set(item_list)) # Make item_list unique.
    matching_items = []
    for item in item_list:
        if desc in world_items[item][DESCWORDS]:
            matching_items.append(item)
    return matching_items


def get_first_item_matching_desc(desc, item_list):
    item_list = list(set(item_list)) # Make item_list unique.
    for item in item_list:
        if desc in world_items[item][DESCWORDS]:
            return item
    return None


def move_direction(direction):
    """A helper function that changes the location of the player."""
    global location

    if direction in world_rooms[location]:
        print('You move to the %s.' % direction)
    else:
        print('You cannot move in that direction.')


class TextAdventureCmd(cmd.Cmd):
    prompt = '\n> '

    def complete_buy(self, text, line, begidx, endidx):
        if SHOP not in world_rooms[location]:
            return []

        item_to_buy = text.lower()
        possible_items = []

        # If the user has only typed "buy" but no item name:
        if not item_to_buy:
            return get_all_first_desc_words(world_rooms[location][SHOP])

        # Otherwise, get a list of all "description words" for shop items
        # matching the command text so far:
        for item in list(set(world_rooms[location][SHOP])):
            for desc_word in world_items[item][DESCWORDS]:
                if desc_word.startswith(text):
                    possible_items.append(desc_word)

        return list(set(possible_items)) # Make list unique.


    def complete_drop(self, text, line, begidx, endidx):
        possible_items = []
        item_to_drop = text.lower()

        # Get a list of all "description words" for each item in the inventory.
        inv_desc_words = get_all_desc_words(inventory)

        for desc_word in inv_desc_words:
            if line.startswith('Drop %s' % (desc_word)):
                return [] # Command is complete.

        # If the user has only typed "drop" but no item name:
        if item_to_drop == '':
            return get_all_first_desc_words(inventory)

        # Otherwise, get a list of all "description words" for inventory items
        # matching the command text so far:
        for desc_word in inv_desc_words:
            if desc_word.startswith(text):
                possible_items.append(desc_word)

        return list(set(possible_items)) # Make list unique.


    def complete_eat(self, text, line, begidx, endidx):
        item_to_eat = text.lower()
        possible_items = []

        # If the user has only typed "eat" but no item name:
        if item_to_eat == '':
            return get_all_first_desc_words(inventory)

        # Otherwise, get a list of all "description words" for edible inventory
        # items matching the command text so far:
        for item in list(set(inventory)):
            for desc_word in world_items[item][DESCWORDS]:
                if (desc_word.startswith(text) and
                    world_items[item].get(EDIBLE, False)):
                    possible_items.append(desc_word)

        return list(set(possible_items)) # Make list unique.


    def complete_look(self, text, line, begidx, endidx):
        possible_items = []
        looking_at = text.lower()

        # Get a list of all "description words" for each item in the inventory.
        inv_desc_words = get_all_desc_words(inventory)
        ground_desc_words = get_all_desc_words(world_rooms[location][GROUND])
        shop_desc_words = get_all_desc_words(world_rooms[location].
            get(SHOP, []))

        for desc_word in (inv_desc_words + ground_desc_words +
                          shop_desc_words +
                          [NORTH, SOUTH, EAST, WEST, UP, DOWN]):
            if line.startswith('look %s' % (desc_word)):
                return [] # Command is complete.

        # If the user has only typed "look" but no item name, show all items
        # on ground, shop and directions:
        if looking_at == '':
            possible_items.extend(
                get_all_first_desc_words(world_rooms[location][GROUND]))
            possible_items.extend(
                get_all_first_desc_words(world_rooms[location].get(SHOP, [])))
            for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
                if direction in world_rooms[location]:
                    possible_items.append(direction)
            return list(set(possible_items)) # Make list unique.

        # Otherwise, get a list of all "description words" for ground items
        # matching the command text so far:
        for desc_word in ground_desc_words:
            if desc_word.startswith(looking_at):
                possible_items.append(desc_word)

        # Otherwise, get a list of all "description words" for items for sale
        # at the shop (if this is one):
        for desc_word in shop_desc_words:
            if desc_word.startswith(looking_at):
                possible_items.append(desc_word)

        # Check for matching directions.
        for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
            if direction.startswith(looking_at):
                possible_items.append(direction)

        # Get a list of all "description words" for inventory items matching
        # the command text so far:
        for desc_word in inv_desc_words:
            if desc_word.startswith(looking_at):
                possible_items.append(desc_word)

        return list(set(possible_items)) # Make list unique.


    def complete_sell(self, text, line, begidx, endidx):
        if SHOP not in world_rooms[location]:
            return []

        item_to_sell = text.lower()
        possible_items = []

        # If the user has only typed "sell" but no item name:
        if not item_to_sell:
            return get_all_first_desc_words(inventory)

        # Otherwise, get a list of all "description words" for inventory
        # items matching the command text so far:
        for item in list(set(inventory)):
            for desc_word in world_items[item][DESCWORDS]:
                if desc_word.startswith(text):
                    possible_items.append(desc_word)

        return list(set(possible_items)) # Make list unique.


    def complete_take(self, text, line, begidx, endidx):
        possible_items = []
        text = text.lower()

        # If the user has only typed "take" but no item name:
        if not text:
            return get_all_first_desc_words(world_rooms[location][GROUND])

        # Otherwise, get a list of all "description words" for ground items
        # matching the command text so far:
        for item in list(set(world_rooms[location][GROUND])):
            for desc_word in world_items[item][DESCWORDS]:
                if (desc_word.startswith(text) and
                    world_items[item].get(TAKEABLE, True)):
                    possible_items.append(desc_word)

        return list(set(possible_items)) # Make list unique.


    # The default() method is called when none of the other do_*() command
    # methods match.
    def default(self, arg):
        print('I do not understand that command. '
              'Type "help" for a list of commands.')


    def do_buy(self, arg):
        """Buy <item> - buy an item at the current location's shop."""
        if SHOP not in world_rooms[location]:
            print('This is not a shop.')
            return

        item_to_buy = arg.lower()

        if item_to_buy == '':
            print('Buy what? Type "list" or "list full" to see a list of '\
                  'items for sale.')
            return

        item = get_first_item_matching_desc(item_to_buy,
                                            world_rooms[location][SHOP])
        if item != None:
            # NOTE - If you wanted to implement money, here is where you would
            # add.
            # Code that checks if the player has enough, then deducts the price
            # from their money.
            print('You have purchased %s.' % (world_items[item][SHORTDESC]))
            inventory.append(item)
            return

        print('"%s" is not sold here. Type "list" or "list full" to see a '\
              'list of items for sale.' % (item_to_buy))


    # These direction commands have a long (i.e. north) and short (i.e. n)
    # form. Since the code is basically the same, I put it in the
    # move_direction() function.
    def do_down(self, arg):
        """Go to the area downwards, if possible."""
        move_direction('down')


    def do_east(self, arg):
        """Go to the area to the east, if possible."""
        move_direction('east')


    def do_north(self, arg):
        """Go to the area to the north, if possible."""
        move_direction('north')


    def do_south(self, arg):
        """Go to the area to the south, if possible."""
        move_direction('south')


    def do_up(self, arg):
        """Go to the area upwards, if possible."""
        move_direction('up')


    def do_west(self, arg):
        """Go to the area to the west, if possible."""
        move_direction('west')


    # Since the code is the exact same, we can just copy the methods with
    # methods with shortened names:
    do_d = do_down
    do_e = do_east
    do_n = do_north
    do_s = do_south
    do_u = do_up
    do_w = do_west


    def do_drop(self, arg):
        """Drop <item> - Drop an item from your inventory onto the ground."""
        # Put this value in a more suitably named variable.
        item_to_drop = arg.lower()

        # Get a list of all "description words" for each item in the inventory.
        inv_desc_words = get_all_desc_words(inventory)

        # Find out if the player doesn't have that item
        if item_to_drop not in inv_desc_words:
            print('You do not have %s in your inventory.' % (item_to_drop))
            return

        # Get the item name that the player's command describes.
        item = get_first_item_matching_desc(item_to_drop, inventory)
        if item != None:
            print('You drop %s.' % (world_items[item][SHORTDESC]))
            inventory.remove(item) # Remove from inventory.
            world_rooms[location][GROUND].append(item) # Add to the ground.


    def do_eat(self, arg):
        """Eat <item> - Eat an item in your inventory."""
        item_to_eat = arg.lower()

        if item_to_eat == '':
            print('Eat what? Type "inventory" or "inv" to see your inventory')
            return

        cant_eat = False

        for item in get_all_items_matching_desc(item_to_eat, inventory):
            if world_items[item].get(EDIBLE, False) == False:
                cant_eat = True
                # There may be other items named this that you can eat,
                # so we continue checking.
                continue
            # NOTE - If you wanted to implement hunger levels, here is where
            # you would add code that changes the player's hunger level.
            print('You eat %s' % (world_items[item][SHORTDESC]))
            inventory.remove(item)
            return

        if cant_eat:
            print('You cannot eat that.')
        else:
            print('You do not have "%s". Type "inventory" or "inv" to see your'\
                  'inventory.' % (item_to_eat))


    def do_exits(self, arg):
        """Toggle showing full exit descriptions or brief exit descriptions."""
        global show_full_exits
        show_full_exits = not show_full_exits
        if show_full_exits:
            print('Showing full exit descriptions.')
        else:
            print('Showing brief exit descriptions.')


    def do_inventory(self, arg):
        """Display a list of items in your possession."""

        if len(inventory) == 0:
            print('Inventory:\n (nothing)')
            return

        # First get a count of each distinct item in the inventory.
        item_count = {}
        for item in inventory:
            if item in item_count.keys():
                item_count[item] += 1
            else:
                item_count[item] = 1

        # Get a list of inventory items with duplicates removed:
        print('Inventory:')
        for item in set(inventory):
            if item_count[item] > 1:
                print('  %s (%s)' % (item, item_count[item]))
            else:
                print('  ' + item)


    do_inv = do_inventory


    def do_list(self, arg):
        """
        List the items for sale at the current location's shop. "List full"
        will show details of the items.
        """
        if SHOP not in world_rooms[location]:
            print('This is not a shop.')
            return

        arg = arg.lower()

        print('For sale:')
        for item in world_rooms[location][SHOP]:
            print('  - %s' % (item))
            if arg == 'full':
                print('\n'.join(textwrap.wrap(world_items[item][LONGDESC],
                                              SCREEN_WIDTH)))


    def do_look(self, arg):
        """
        Look at an item, direction, or the area:
            'look' - Display the current area's description.
            'look <direction>' - Display the description of the area in that
            direction.
            'look exits' - Display the description of all adjacent areas.
            'look <item>' - Display the description of an item on the ground
            or in your inventory.
        """
        looking_at = arg.lower()
        if looking_at == '':
            # "Look" will re-print the area description.
            display_location(location)
            return

        if looking_at == 'exits':
            for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
                if direction in world_rooms[location]:
                    print('%s: %s' % (direction.title(),
                                      world_rooms[location][direction]))
            return

        if looking_at in ('north', 'west', 'east', 'south', 'up', 'down', 'n'
                          'w', 'e', 's', 'u', 'd'):
            if looking_at.startswith('n') and NORTH in world_rooms[location]:
                print(world_rooms[location][NORTH])
            elif looking_at.startswith('w') and WEST in world_rooms[location]:
                print(world_rooms[location][WEST])
            elif looking_at.startswith('e') and EAST in world_rooms[location]:
                print(world_rooms[location][EAST])
            elif looking_at.startswith('s') and SOUTH in world_rooms[location]:
                print(world_rooms[location][SOUTH])
            elif looking_at.startswith('u') and UP in world_rooms[location]:
                print(world_rooms[location][UP])
            elif looking_at.startswith('d') and DOWN in world_rooms[location]:
                print(world_rooms[location][DOWN])
            else:
                print('There is nothing in that direction.')
            return

        # See if the item being looked at is on the ground at this location.
        item = get_first_item_matching_desc(looking_at,
                                            world_rooms[location][GROUND])
        if item != None:
            print('\n'.join(textwrap.wrap(world_items[item][LONGDESC],
                            SCREEN_WIDTH)))
            return

        print('You do not see that nearby.')


    # A very simple "quit" command to terminate the program.
    def do_quit(self, arg):
        """Quit the game."""
        # This exits the Cmd application loop in TextAdventureCmd.cmdloop().
        return True


    def do_sell(self, arg):
        """Sell <item> - Sell an item at the current location's shop."""
        if SHOP not in world_rooms[location]:
            print('This is not a shop.')
            return

        item_to_sell = arg.lower()

        if item_to_sell == '':
            print('Sell what?'\
                  'Type "inventory" or "inv" to see your inventory.')
            return

        for item in inventory:
            if item_to_sell in world_items[item][DESCWORDS]:
                # NOTE - If you wanted to implement money, here is where you
                # would add code that gives the player money for selling the
                # item.
                print('You have sold %s.' % (world_items[item][SHORTDESC]))
                inventory.remove(item)
                return

        print('You do not have "%s". Type "inventory" or "inv" to see your'\
              'inventory.' % (item_to_sell))


    def do_take(self, arg):
        """Take <item> - Take an item on the ground."""
        # Put this value in a more suitably named variable.
        item_to_take = arg.lower()

        if item_to_take == '':
            print('Take what? Type "look" the items on the ground here.')
            return

        cant_take = False

        # Get the item name that the player's command describes.
        for item in get_all_items_matching_desc(item_to_take,
                                                world_rooms[location][GROUND]):
            if world_items[item].get(TAKEABLE, True) == False:
                cant_take = True
                # There may be other items named this that you can take, so we
                # continue checking.
                continue
            print('You take %s.' % (world_items[item][SHORTDESC]))
            # Remove from the ground.
            world_rooms[location][GROUND].remove(item)
            inventory.append(item) # Add to inventory.
            return

            if cant_take:
                print('You cannot take "%s".' % (item_to_take))
            else:
                print('That is not on the ground.')


    def help_combat(self):
        print('Combat is not implemented in this program.')


if __name__ == '__main__':
    print('Text Adventure Demo!')
    print('====================')
    print('\n')
    print('(Type "help" for commands.)')
    print('\n')
    display_location(location)
    TextAdventureCmd().cmdloop()
    print('Thanks for playing!')
