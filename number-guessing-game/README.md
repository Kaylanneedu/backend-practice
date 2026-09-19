# Number Guessing Game
A number guessing CLI game with hints, timer and high score tracking.

Solution to the [Number Guessing Game](https://roadmap.sh/projects/number-guessing-game) challenge from [roadmap.sh](https://roadmap.sh).

## Features

- 3 difficulty levels (Easy, Medium, Hard)
- Hint system (parity, range, divisibility clues)
- Timer tracking how long each round takes
- Persistent high score per difficulty level
- Replay without restarting the program

## How to Run

**Requirements:** Python 3.x

```bash
git clone https://github.com/Kaylanneedu/backend-practice.git
cd number-guessing-game
python main.py
```

## Project Structure

```
number-guessing-game/
├── main.py               # entry point, game loop and difficulty menu
├── game.py               # core round logic
├── hints.py              # hint functions
├── highscore.py          # persistence of high scores (JSON)
└── config.py             # difficulty settings
```
