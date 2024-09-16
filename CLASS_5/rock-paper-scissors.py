#THE RULES OF ROCK PAPER SCISSORS
import random



def prompt():
    #BUILD OUR INPUT
    print("WELCOME TO OUR GAME OF ROCK PAPER SCISSORS\n"
          "THE RULES ARE SIMPLE\n"
          "CHOOSE 1 - ROCK\n"
          "CHOOSE 2- PAPER\n"
          "CHOOSE 3 - SCISSORS\n")

options = ["rock", "paper", "scissors"]

def user_input():
    while True:
        try:
            player = input("Pick a number between 1 - 3: ")
            #clean the input and make that the position in our choice list to use,
            idx = int(player)
            if 1 <= idx <= 3:
                # remember list index is length - 1 hence the subtraction
                option = options[idx - 1]
                break
            print("You have to pick between 1 - 3")
        except ValueError:
            print("Invalid choice, Try again")
    return option


def play_game():
    while True:
        #Ask for input from the user
            player_choice = user_input()
            computer_choice = random.choice(options)
            is_winner = False

            #CONDITIONS FOR OUR GAME
            if computer_choice == "scissors" and player_choice == "rock":
                is_winner = True
            elif computer_choice == "paper" and player_choice == "scissors":
                is_winner = True
            elif computer_choice == "rock" and player_choice == "paper":
                is_winner = True
            elif computer_choice == player_choice:
                print("Its a draw,Play Again")
                continue
            else:
                is_winner = False

            print(f"You chose {player_choice} and computer chose {computer_choice}")

            if is_winner:
                print("You Win!")
                break
            else:
                print("You Lose, Play Again")

#create a function that calls these functions so you can play the game, also see if you can
#tweak the game so you keep playing till you loose and a prompt to ask if you want to play again