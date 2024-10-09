# input_numbers = input("Enter numbers separated by spaces: ")

# #  Convert the input string to a list of integers
# numbers = list(map(int, input_numbers.split()))

# # Sorting numbers in ascending order using sorted()
# ascending_numbers = sorted(numbers)
# print(ascending_numbers)

# #Sorting numbers in descending order using sorted()
# descending_numbers = sorted(numbers, reverse=True)
# print(descending_numbers)


#Sorting numbers in ascending order (in-place)
#numbers.sort()
# print(numbers)

#Sorting numbers in descending order (in-place)
#numbers.sort(reverse=True)
#print(numbers)


#finding the largest number in a list
#number= [43,89,67,56,12]
#largest_number = max(number)
#print(largest_number)

#finding the sum of numbers in a list
# list1= [10,20,30,40,50]
# list1_sum = sum(list1)
# print(list1_sum)

#creating duplicate lists
#list2 = [23,45,67,-10,23,50,-10]
#duplicated_list= list2.copy()
#print(duplicated_list)

# #a a list of numbers and iterates through it using a for loop
# numbers = [42, 23, 17, 56, 30, 89, 4]

# for index, number in enumerate(numbers):
#     print(f"Index {index}: {number}")


# # Create a tuple to store the student's name, age, and grade
# student_info = ("John Doe", 20, "A")

# # Print the entire tuple
# print( student_info)



operators = ("+", "-", "*", "/")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:  # Avoid division by zero
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed"
    else:
        return "Invalid operator selected"


print( operators)


operator = input("Choose an operator (+, -, *, /): ")

result = calculate(num1, num2, operator)
print(f"\nThe result of {num1} {operator} {num2} is: {result}")


