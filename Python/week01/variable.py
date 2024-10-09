import random

def guess_the_number():
    # Select a random number between 1 and 100
    target_number = random.randint(1, 100)

    

    while True:
        choice = input("Enter a number between 1 and 100: ")

        # Check if the input is a valid integer
        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        choice = int(choice)

        if choice < target_number:
            print("Higher")
        elif choice > target_number:
            print("Lower")
        else:
            print(f"Correct! The target number was {target_number}.")
            break  # Exit the loop once the correct guess is made

guess_the_number()


