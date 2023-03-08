#HOT OR COLD GAME
import random

def HotOrCold():
    game_on = True

    while game_on:
        number = random.randint(0, 1000)
        print("Hello there, I am thinking of a number between 0 and 1000. Can you guess it?")
        print(number)
        count = 0

        while True:
            try:
                guess = int(input("What is your guess, player?: "))
                count += 1

                if (guess < 0 or
                        guess > 1000):
                    print("The number must be between 0 and 1000")

                elif guess == number:
                    print("THAT'S IT! YOU WON in", count, "guesses!")
                    break

                elif abs(number - guess) < 10:
                    print("HOT")

                elif abs(number - guess) < 100:
                    print("You're getting there")

                else:
                    print("Cold.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
                play_again = input("Do you want to play again? Y or N: ").upper()
                if play_again == "Y":
                    break
                elif play_again == "N":
                    game_on = False
                    break
                else:
                    print("Please enter Y or N")
    print("Thanks for playing!")






HotOrCold()



