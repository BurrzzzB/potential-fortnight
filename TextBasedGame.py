def show_instructions():
   print("Dragon Text Adventure Game")
   print("Collect 6 items to win the game, or be eaten by the dragon.")
   print("Move commands: go South, go North, go East, go West")
   print("Add to Inventory: get 'item name'")


def show_state(inventory, rooms, state):
    print('Inventory: ', inventory)
    print('You see a ', rooms[state][0])
    print("--------------------------------")
    cmd, direction = input('Enter your move: ').split()
    return direction


rooms = {
    'Main Castle Entrance': {'South': 'Dining Room', 'West': 'Library', 'North': 'Armory', 'East': 'Dungeon'},
    'Library': {'East': 'Main Castle Entrance'},
    'Princess Room': {'West': 'Armory'},
    'Armory': {'East': 'Princess Room', 'South': 'Main Castle Entrance'},
    'Dining Room': {'North': 'Main Castle Entrance', 'East': 'Kitchen'},
    'Kitchen': {'West': 'Dining Room'},
    'Dungeon': {'North': 'Dragon Room', 'West': 'Main Castle Entrance'},
    'Dragon Room': {'South': 'Dungeon'},
}
weapons = {
    "Main Castle Entrance": "Map",
    "Library": "Mission Scroll",
    "Armory": "Enchanted Sword",
    "Dragon Room": "Lock",
    "Dungeon": "Shield",
    "Kitchen": "Key",
    "Princess Room": "Villain",
    "Dining Room": "none"
}
state = 'Main Castle Entrance'
inventory = []


def get_new_state(state, direction):
    new_state = state
    for i in rooms:
        if i == state:
            if direction in rooms[i]:
                new_state = rooms[i][direction]

    return new_state


while 1:
    print('You are in the ', state)
    if state == 'Princess Room':
        print('Battling with the Princess', end='')
        for i in range(50):
            for j in range(1000000):
                pass
            print(".", end='', flush=True)
        print()
        if len(inventory) == 6:
            print('You won - congratulations')
        else:
            print('Sorry, you lost - be better armed next time')
        break

    print('Available to you in this room is', state)
    print('You currently have', inventory)
    direction = input('Enter item you want OR direction to go OR exit to give up: ')
    if direction.lower() == weapons[state].lower():
        if weapons[state] not in inventory:
            inventory.append(weapons[state])
        continue
    direction = direction.capitalize()
    if direction == 'Exit':
        exit(0)
    if direction == 'East' or direction == 'West' or direction == 'North' or direction == 'South':
        new_state = get_new_state(state, direction)
        if new_state == state:
            print('There is a fearsome darkness in that direction quickly enter other direction!')
        else:
            state = new_state
    else:
        print('Invalid direction!!')
