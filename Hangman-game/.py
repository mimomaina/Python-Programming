import random

words = [
    'python', 'javascript', 'hangman', 'computer', 'program', 'developer',
    'algorithm', 'function', 'variable', 'terminal', 'keyboard', 'science',
    'challenge', 'github', 'coding', 'project', 'website', 'network'
]

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = random.choice(words)
    guessed_letters = set()
    wrong_attempts = 0
    max_wrong = 6

    print("Welcome to Hangman!")
    print("Try to guess the word. You have 6 attempts if you make wrong guesses.\n")
    print(f"Your word: {'_' * len(word)}")

    while wrong_attempts < max_wrong:
        guess = input("\nEnter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_attempts += 1
            print(f"Wrong guess! '{guess}' is not in the word.")
            print(f"Attempts left: {max_wrong - wrong_attempts}")

        current_display = display_word(word, guessed_letters)
        print(f"Word: {current_display}")

        if '_' not in current_display:
            print("\n🎉 Congratulations! You've guessed the word!")
            print(f"The word was: {word}")
            break
    else:
        print("\n💀 You've run out of attempts!")
        print(f"The word was: {word}")
        print("You lost. The monster got you!")

hangman()