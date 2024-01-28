import random
import os


def main():
    spaces = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player = 'X'
    computer = 'O'
    running = True

    while(running):
        os.system('clear')
        drawBoard(spaces)

        playerMove(spaces, player)
        os.system('clear')
        drawBoard(spaces)
        if checkWinner(spaces, player, computer):
            running = False
            break
        elif checkTie(spaces):
            running = False
            break

        computerMove(spaces, computer)
        os.system('clear')
        drawBoard(spaces)
        if checkWinner(spaces, player, computer):
            running = False
            break
        elif checkTie(spaces):
            running = False
            break


def drawBoard(spaces):
    print()
    print("     |     |     ")
    print(f"  {spaces[0]}  |  {spaces[1]}  |  {spaces[2]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {spaces[3]}  |  {spaces[4]}  |  {spaces[5]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {spaces[6]}  |  {spaces[7]}  |  {spaces[8]}  ")
    print("     |     |     ")
    print()


def playerMove(spaces, player):
    while True:
        number = int(input("Enter a move (1-9): ")) - 1
        if 0 <= number <= 8 and spaces[number] == ' ':
            spaces[number] = player
            break


def computerMove(spaces, computer):
    while True:
        try:
            number = random.randint(1, 9)
            if spaces[number] == ' ':
                spaces[number] = computer
                break
        except IndexError:
            continue


def checkWinner(spaces, player, computer):
    if spaces[0] != ' ' and spaces[0] == spaces[1] and spaces[1] == spaces[2]:
        if spaces[0] == player:
            print("You Win")
        else:
            print("You Lose")
    elif spaces[3] != ' ' and spaces[3] == spaces[4] and spaces[4] == spaces[5]:
        if spaces[3] == player:
            print("You Win")
        else:
            print("You Lose")
    elif spaces[6] != ' ' and spaces[6] == spaces[7] and spaces[7] == spaces[8]:
        if spaces[6] == player:
            print("You Win")
        else:
            print("You Lose") 
    elif spaces[0] != ' ' and spaces[0] == spaces[3] and spaces[3] == spaces[6]:
        if spaces[0] == player:
            print("You Win")
        else:
            print("You Lose")
    elif spaces[1] != ' ' and spaces[1] == spaces[4] and spaces[4] == spaces[7]:
        if spaces[1] == player:
            print("You Win")
        else:
            print("You Lose")
    elif spaces[2] != ' ' and spaces[2] == spaces[5] and spaces[5] == spaces[8]:
        if spaces[2] == player:
            print("You Win")
        else:
            print("You Lose")
    elif spaces[0] != ' ' and spaces[0] == spaces[4] and spaces[4] == spaces[8]:
        if spaces[0] == player:
            print("You Win")
        else:
            print("You Lose")
    elif spaces[2] != ' ' and spaces[2] == spaces[4] and spaces[4] == spaces[6]:
        if spaces[2] == player:
            print("You Win")
        else:
            print("You Lose")
    else:
        return False
    
    return True


def checkTie(spaces):
    for space in spaces:
        if space == ' ':
            return False
    
    print("It's a Tie")
    return True


if __name__ == "__main__":
    main()
