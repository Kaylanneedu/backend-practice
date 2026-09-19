from random import randint, choice
import time
from hints import hints
from highscore import load_highscores, save_highscores

def play(chances, level_name):
    print(f"""
            -------------------------------------------------------------
            Great! You have selected the {level_name} difficulty level.
            You have {chances} chances to guess the correct number.
            Let's start the game!
            --------------------------------------------------------------
            """)
    
    answer = randint(1, 100)
    attempts = 1
    start_time =time.time()
    available_hints = hints.copy()
    
    while chances > 0:
        guess = input("Enter your guess (or 'h' for a hint):  ")
        print()
        if guess.lower() == 'h':
            if available_hints:
                chosen = choice(available_hints)
                available_hints.remove(chosen)
                print(f"Hint: {chosen(answer)}")
            else:
                print("No more hints available!")
            continue
    
        try:
            guess = int(guess)
            if not (1 <= guess <= 100):
                print("Invalid input! Please enter a number between 1 and 100.")
                continue
            else:
                if guess < answer:
                    print(f"Incorrect! The number is greater than {guess}.")
                    chances -= 1
                    attempts += 1
                elif guess > answer:
                    print(f"Incorrect! The number is less than {guess}.")
                    chances -= 1
                    attempts += 1
                else:
                    print(f"Congratulations! You guessed the correct number in {attempts} attempts")
                    elapsed = time.time() - start_time
                    print(f"Time taken to WIN!: {elapsed:.2f} seconds.")

                    scores = load_highscores()
                    current_best = scores.get(level_name)

                    if current_best is None or attempts < current_best:
                        scores[level_name] = attempts
                        save_highscores(scores)
                        print(f"New high score for {level_name}: {attempts} attempts!")
                    else:
                        print(f"Current high score for {level_name} remains: {current_best} attempts.")

                    break
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    if chances == 0:
            print(f"\nGAME OVER!, You ran out of chances. The number was {answer}.")
            elapsed = time.time() - start_time
            print(f"Time taken to LOSE!: {elapsed:.2f} seconds.")
    
    
