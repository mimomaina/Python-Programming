file = open('mbox.txt')

# count = 0
# for line in file:
#     count =count +1
# print(f"line count:{count}")

# prompt=input("Enter file name: ")
# try:
#     file=open(prompt)
#     for word in file:
#         if word .startswith('From'):
#         #print(word)
#             email= word.find('@')
#             after = word.find(' ',email)
#             host=word[email+1:after]
#             print(host)
# except:("Not found")

#writing into a file
file=open('sample txt','w')
text='sample txt here'
file.write(text)
#print(file)
