from random import randint
from art import logo
from art import logo2

# GLOBAL VARIABLES
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5            

turns = 0

# Function to check user's guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Compara 'answer' con 'guess', y devuelve (return) el numero de oportunidades (turns) que le quedan """
    if user_guess > actual_answer:
        print("-Too high.")
        # inside the check_answer() function, if it's too high, if it's too low, then we have to deduct the number of turns they have. Now because this is a global variable, we need to use 'return'.
        return turns - 1
    elif user_guess < actual_answer:
        print("-Too low.")
        return turns - 1
    else:
        print(f"Correct mate, the number is {actual_answer}. You win!!!")
    
# Function to set the difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return  EASY_LEVEL_TURNS
    else:
        return  HARD_LEVEL_TURNS

def game():
    print(logo)
    print(logo2)
    # Choosing a random number between 1 and 100
    print("-Welcome to the Guessing Game mate!")
    print("-I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"-Just to let you know that the game is working, the correct answer is [{answer}] however, check UX.")


    turns = set_difficulty()
    


    # If we set the while condition as while guess is not equal to answer, then that pretty much guarantees that these lines of code will keep going until the user actually gets the right answer.
    guess = 0
    # Reapeat the guessing functionality if they get it wrong
    while guess != answer:
        print(f"-You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("make a guess: \n"))
        turns = check_answer(guess, answer, turns)
        # When the player runs out of attempts we need to stop the game and tell them that they've lost.
        if turns == 0:
            print("-You run out of attempts, You lose...")
            # As we have our game inside a function which is being called <--def game(), we can just write 'return' for it to exit and end the function.
            return
        # This is for the UX. If they have any attempt left we can print a message
        elif guess != answer:
            print("-guess again, mate.")
            



        #track the number of turns and reduce by 1 if they guess wrong 

        
game()