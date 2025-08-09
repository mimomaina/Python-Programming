import random

def play_rps():
    choices = ['rock', 'paper', 'scissors']
    rounds_to_win = 2 if input("Play best of 3 or 5? (3/5): ").strip() == '3' else 3
    user_score = 0
    computer_score = 0

    while user_score < rounds_to_win and computer_score < rounds_to_win:
        user_choice = input("\nChoose rock, paper, or scissors: ").lower()
        if user_choice not in choices:
            print("Invalid choice. Try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        if user_score == rounds_to_win:
            print("\nYou won the game!")
            break
        elif computer_score == rounds_to_win:
            print("\nComputer won the game!")
            break

    print("Game over. Thanks for playing!")

play_rps()