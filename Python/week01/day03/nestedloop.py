# import random
# import string

# def generate_puzzle (grid_size,correct_letter,):
#     grid= [(random_choice)  for_in range (grid_size)]:
# correct_letter= random.choice 
# grid[0][0] = correct_choice
# grid[1][1] =correct_choice
# grid[2][2] =correct_choice

# return grid_size ,correct_letter

# grid_size = 3
#  puzzle_grid, correct_letter = generate_puzzle(grid_size)
# print(grid)



# text = 'PYTHON'
# text_length = len(text)
# for i in range(text_length):
#     print("  "*i,text[i])


# def main():
#     grid_size = 5  
#     correct_word = "PYTHON"

    
#     grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]

    
#         for i in range(len(correct_word)):



# # Define the grid size and the correct word
# grid_size = 5  # Size of the grid (you can change this)
# correct_word = "HELLO"  # The hardcoded word to be placed diagonally

# # Initialize the grid with a placeholder (".")
# grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]

# # Place the correct word diagonally in the grid
# for i in range(len(correct_word)):
#     grid[i][i] = correct_word[i]

# # Print the grid with increasing indentation
# for i, row in enumerate(grid):
#     print("  " * i + " ".join(row))




import random

 

options = ["Rock", "Paper", "Scissors"]

 

user_choice = input("Choose Rock, Paper, or Scissors: ")

computer_choice = random.choice(options)

 

print("You chose: ", user_choice)

print("Computer chose: ", computer_choice)

 

if user_choice == computer_choice:

    print("It's a tie!")

elif user_choice == "Rock" and computer_choice == "Scissors":

    print("You win!")

elif user_choice == "Paper" and computer_choice == "Rock":

    print("You win!")

elif user_choice == "Scissors" and computer_choice == "Paper":

    print("You win!")

else:

    print("Computer wins!")


    