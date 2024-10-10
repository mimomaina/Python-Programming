#can not be duplicated
#orders by default
# student_info = {12,'John','John'}
# print(student_info)

# empty = set()#empty set

#adding  in sets
# numbers = {23,3,5,98}
# number.add(10)
# print(numbers)

#updating sets
# numbers = {23,3,5,98}
# new_nums= {1,4,6}
# numbers.update(new_nums)
# print(numbers)

#removing an element set
# numbers = {23,3,5,98}
# numbers.discard(98)
# print(numbers)

#iterating sets
# numbers = {23,3,5,98}
# for number in numbers:
#     print(number)

#finding number of set elements
#numbers = {23,3,5,98}
#num=len(numbers)
# print(num)

#set operators
#union operators- all elements included
# setA={1,3,5}
# setB={0,2,4}
# union=setA|setB
# print(union)

#intersection - only similar elements are included
# setA={1,3,5}
# setB={1,2,4}
# intersection= setA&setB
# print(intersection)

#difference between sets
# setA={1,3,5}
# setB={1,2,4}

# difference= setA-setB
# print(difference)

# difference=setB-setA
# print(difference)

#symetric difference-wihout common difference
# symetric = setA^setB
# print(symetric)

#check if 2 sets are equal
setA={1,3,5}
setB={3,5,1}
if setA==setB:
    print(f'setA and setB are equal')
else:
    print('The sets are not equal')