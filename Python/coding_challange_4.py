#checking for positive and negative numbers
# def check_number(num):
#     if num > 0:
#         return "Positive"
#     elif num < 0:
#         return "Negative"
#     else:
#         return "Zero"
# print (check_number(10))      
# print (check_number(-3))

#area of a rectangle
# def rectangle_area(length, width):
#     return length * width
# print(rectangle_area(4,7))

#area of a circle
# import math

# def circle_area(radius):
#     return math.pi * radius ** 2
# print(circle_area(6))

#area of a triangle
# def triangle_area(base, height):
#     return 0.5 * base * height
# print(triangle_area(9,8))

# #area of a square
# def square_area(side):
#     return side ** 2
# print(square_area(6))

#grading system
def calculate_grade(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    elif score < 60:
        return "F"
    else:
        return "Invalid score"  # To handle any invalid inputs like scores above 100 or negative values

print(calculate_grade(95))  
print(calculate_grade(85))  
print(calculate_grade(75))  
print(calculate_grade(65))  
print(calculate_grade(50))  
print(calculate_grade(105)) 
print(calculate_grade(-10))