import random

menu_prompt = """
WELCOME TO ROCK, PAPER, SCISSORS!!

Would you like to play? (y/n/yes/no): 

"""

decision = input(menu_prompt).strip().upper()

count_bot = 0
count_player = 0

while not (decision == 'N' or decision == 'NO'):
    if decision == 'Y' or decision == 'YES':
        options = ['rock', 'paper', 'scissors']

        bot = random.choice(options)
        player = input("Enter (rock, paper, scissors): ")

        if bot == player:
            print(f"{bot} vs {player}\nIts a Draw!")
        elif bot == 'rock' and player == 'paper':
            print(f"{bot} vs {player}\nPlayer capture Bot")
            count_player += 1
        elif bot == 'rock' and player == 'scissors':
            print(f"{bot} vs {player}\nBot smashed Player")
            count_bot += 1
        elif bot == 'paper' and player == 'rock':
            print(f"{bot} vs {player}\nBot capture Player ")
            count_bot += 1
        elif bot == 'paper' and player == 'scissors':
            print(f"{bot} vs {player}\nPlayer cut Bot")
            count_player += 1
        elif bot == 'scissors' and player == 'rock':
            print(f"{bot} vs {player}\nPlayer smashed Bot")
            count_player += 1
        elif bot == 'scissors' and player == 'paper':
            print(f"{bot} vs {player}\nBot cut player")
            count_bot += 1
        else:
            print("Wrong election, please try again")
        print("BOT PLAYER\n",
              count_bot, " - ", count_player)

    else:
        print("Wrong input, please type one the options.")

    decision = input("Would you like to play? (y/n)\n").strip().upper()
    if not (decision != 'Y' or decision != 'YES'):
        break
