#simple calculator
# def calculator():
#     # Get user input for two numbers and the operator
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     operator = input("Enter the operator (+, -, *, /): ")

#     # Perform the operation based on the operator
#     if operator == '+':
#         print(f"{num1} + {num2} = {num1 + num2}")
#     elif operator == '-':
#         print(f"{num1} - {num2} = {num1 - num2}")
#     elif operator == '*':
#         print(f"{num1} * {num2} = {num1 * num2}")
#     elif operator == '/':
#         if num2 != 0:
#             print(f"{num1} / {num2} = {num1 / num2}")
#         else:
#             print("Error: Division by zero is not allowed.")
#     else:
#         print("Invalid operator!")

# # Run the calculator
# calculator()



#Printing random numbers between 1 to 100
# import random

# # Generate a random number between 1 and 100
# random_number = random.randint(1, 100)

# # Print the random number
# print("Random number between 1 and 100:", random_number)


import math

# Ask the user to input a number
number = float(input("Enter a number: "))

# Calculate the square root using math.sqrt
square_root = math.sqrt(number)

# Print the result
print(f"The square root of {number} is: {square_root}")


