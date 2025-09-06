import random
def number_guessing_game():
    print("welcome to the number guessing game!")
    print("I have chosen a number between 1 to 100, Can you guess it?")

    secret_number=random.randint(1,100)
    attempts=0

    while True:
        try:
            guess=int(input("Enter your guess: "))
            attempts+=1

            if guess< secret_number:
                print("Number you guessed is too low! Try again")

            elif guess> secret_number:
                print("Number you guessed is too high! Try again")
            else:
                print(f"congratulations! you guessed it {attempts}attempts.")
                break
        except ValueError:
            print("please enter a number between 1 to 100")

number_guessing_game()