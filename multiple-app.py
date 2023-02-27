#MULTIPLE PLAYER GAME 

import random 
import sys
import time 

DICE = 6

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

def print_msg():
    msg = """

    SNAKE AND LADDERS 

    MAXIMUM 4 PLAYERS ALLOWED

    HIT ENTER TO PLAY:

    """

    print(msg)

def dice_value():
    time.sleep(1)
    diceValue = random.randint(1,DICE)
    print("Rolling Dice Value:" + str(diceValue))
    return diceValue

def player_names():
    player = None
    player = input("Enter Player Name: ").strip()
    return player

def snakeBite(oldPosition, newPosition, currentPlayer):
    print("\n" + currentPlayer + " SNAKE BITE ---- DOWN FROM " + str(oldPosition) + " TO " + str(newPosition))


def ladderJump(oldPosition, newPosition, currentPlayer):
    print("\n" + currentPlayer + " LADDER JUMP ---- UP FROM " + str(oldPosition) + " TO " + str(newPosition))

def snakeLadder(playerName, currentPosition, diceValue):
    time.sleep(1)
    oldPosition = currentPosition
    currentPosition= currentPosition + diceValue

    if currentPosition > 100:
        print(str(100 - oldPosition) + "TO GO")
        return oldPosition
    print("\n" + playerName + " MOVES FROM " + str(oldPosition) + " TO " + str(currentPosition))

    if currentPosition in snakes:
        finalPosition =  snakes.get(currentPosition)
        snakeBite(currentPosition, finalPosition, playerName)
    
    elif currentPosition in ladders:
        finalPosition = ladders.get(currentPosition)
        ladderJump(currentPosition, finalPosition, playerName)
    
    else:
        finalPosition = currentPosition
    
    return finalPosition

def checkWin(playerName, currentPosition):
    time.sleep(1)
    if currentPosition == 100:
        print("\n\n" + playerName + "WINS")
        sys.exit(1)

def gameStart():
    print_msg()
    time.sleep(1)
    n = int(input("Enter Number of Players"))
    while n > 4:
        n = int(input("Re-Enter Number of Players"))
    players = []
    for i in range(n):
        playerName = player_names()
        players.append(playerName)

    time.sleep(1)

    for i in players:
        print(players[i])

    playerOneCP = 0
    playerTwoCP = 0

    while True:
        time.sleep(1)
        enterInput = input("\n\nPress Enter to Continue ")
        diceValue = dice_value()
        print("\n MOVING....")
        playerOneCP = snakeLadder(playerOne, playerOneCP, diceValue)

        checkWin(playerOne, playerOneCP)

        time.sleep(1)
        enterInput = input("\n\n Press Enter to Continue ")
        diceValue = dice_value()
        print("\n MOVING....")
        playerTwoCP = snakeLadder(playerTwo, playerTwoCP, diceValue)

        checkWin(playerOne, playerOneCP)

if __name__ == "__main__":
    gameStart()


