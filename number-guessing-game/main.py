from config import level
from game import play

print(f"""
---------------------------------------------
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
---------------------------------------------
""")

print("""
---------------------------------------------
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
---------------------------------------------
""")

while True:
    while True:
        difficulty = input("Enter your choice: ")
        if difficulty.lower() == 'q':
            exit()
        try:
            difficulty = int(difficulty)
            if difficulty in [1, 2, 3]:
                break
            else:
                print("Invalid input! Please enter a number between 1 and 3 or press q to quit.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 3 or press q to quit.")

    level_name, chances = level[difficulty]
    play(chances, level_name)

    print("\nDo you want to play again? [yes] to continue or [any button] to exit")
    play_again = input().lower()
    if play_again != "yes":
        exit()

    
