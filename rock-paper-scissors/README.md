# Rock Paper Scissors Game

A simple yet fun command-line Rock-Paper-Scissors game where you challenge the computer in a best-of-3 or best-of-5 match. The game uses Python's `random` module to simulate the computer's moves and determines the winner based on classic game rules.

## 🎮 How to Play

1. Run the script.
2. Choose whether you want to play a **best of 3** or **best of 5** game.
3. Enter your move: `rock`, `paper`, or `scissors`.
4. The computer will make its random choice.
5. The winner of each round is determined:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock
6. Points are tracked per round. The first to reach the required wins (2 out of 3 or 3 out of 5) wins the game.
7. The game ends early if one player cannot be caught by the other.

## 🛠️ Requirements

- Python 3.x

No external libraries are needed — only the built-in `random` module is used.

## 🚀 How to Run

1. Clone or download the project.
2. Open a terminal in the project directory.
3. Run the game:

```bash
python rps_game.py
