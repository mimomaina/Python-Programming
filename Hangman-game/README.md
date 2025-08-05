# Hangman Game

A classic command-line **Hangman** game built in Python! Test your vocabulary by guessing letters to reveal a hidden word — but be careful: make too many wrong guesses and the monster wins!

## 🎮 How to Play

1. The game randomly selects a secret word from a predefined list.
2. The word is displayed as underscores (`_`), one per letter.
3. You guess one letter at a time:
   - If the letter is in the word, it's revealed in all correct positions.
   - If not, it counts as a wrong attempt.
4. You have **6 wrong attempts**. On the 6th failure, the game ends and you lose.
5. If you reveal all letters before hitting 6 wrong guesses, you win!

## 🛠️ Requirements

- Python 3.x
- No external libraries required (pure Python)

## 🚀 How to Run

1. Save the code to a file, e.g., `hangman.py`
2. Open your terminal or command prompt
3. Run the game:

```bash
python hangman.py
