import random
import curses

# Define the snakes and ladders on the game board
snakes = {
    39 : 3,
    27 : 7,
    50 : 34,
    35 : 5,
    66 : 24,
    73 : 12,
    26 : 63,
    99 : 26,
    97 : 86,
    89 : 67
}

ladders = {
    2 : 23,
    7 : 29,
    30 : 32,
    28 : 77,
    22 : 49,
    44 : 58,
    54 : 69,
    70 : 90,
    87 : 93,
    80 : 83
}
# Get the number and names of players from the user
num_players = int(input("Enter the number of players: "))
players = []
for i in range(num_players):
    name = input("Enter player {} name: ".format(i+1))
    players.append({"name": name, "position": 0})

# Initialize the game board GUI using the curses module
board = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
board.clear()

# Define a function to display the game board
def display_board():
    board.clear()
    board.addstr("   _________________\n", curses.color_pair(1))
    for i in range(10):
        if i % 2 == 0:
            board.addstr("  |", curses.color_pair(1))
        else:
            board.addstr(" |", curses.color_pair(1))
        for j in range(10):
            if i % 2 == 0:
                square_num = (i * 10) + j + 1
            else:
                square_num = (i * 10) + (9 - j) + 1
            players_on_square = []
            for player in players:
                if player["position"] == square_num:
                    players_on_square.append(player["name"])
            if square_num in snakes:
                board.addstr(str(square_num).zfill(2), curses.color_pair(2) | curses.A_BOLD)
            elif square_num in ladders:
                board.addstr(str(square_num).zfill(2), curses.color_pair(1) | curses.A_BOLD)
            else:
                board.addstr(str(square_num).zfill(2), curses.color_pair(1))
            if players_on_square:
                board.addstr(" [" + ",".join(players_on_square) + "]", curses.color_pair(1))
            else:
                board.addstr("   ", curses.color_pair(1))
            if i % 2 == 0 and j == 9:
                board.addstr("|", curses.color_pair(1))
            elif i % 2 == 1 and j == 0:
                board.addstr("|", curses.color_pair(1))
        board.addstr("\n")
    board.addstr("   -----------------\n", curses.color_pair(1))

# Define the main
# Define the main game loop
def play_game():
    while True:
        # Display the game board
        display_board()

        # Get input from the player
        for player in players:
            board.addstr("\n{}, it's your turn. Press ENTER to roll the die.".format(player["name"]))
            board.getch()
            roll = random.randint(1, 6)
            board.addstr("\n{} rolls a {}.".format(player["name"], roll))

            # Move the player's position and handle snakes and ladders
            player["position"] += roll
            if player["position"] > 100:
                player["position"] = 100
            if player["position"] in snakes:
                board.addstr("\n{} lands on a snake and slides down to position {}!".format(player["name"], snakes[player["position"]]))
                player["position"] = snakes[player["position"]]
            elif player["position"] in ladders:
                board.addstr("\n{} climbs a ladder to position {}!".format(player["name"], ladders[player["position"]]))
                player["position"] = ladders[player["position"]]
            elif player["position"] == 100:
                board.addstr("\n{} wins the game!".format(player["name"]))
                curses.endwin()
                return

# Start the game
play_game()
