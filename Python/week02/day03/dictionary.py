#use {}
#{"key":value}
#should have unique key. Otherwise it prints the last key+its value.
# dictionary = {"Peter":24,"John":36,"Ruth":20}
# print(dictionary)

#printing keys
# for i in dictionary:
#     print(i)

# dictionary = {"Peter":24,"John":36,"Ruth":20}
# for i,j in dictionary.items():
#     print(f'Name:{i}, Age :{j}')


"""""
Write a program that reads the words in words.txt and stores them as keys in a dictionary.
It doesn’t matter what the values are. Then you can use the in operator as a fast way to check
whether a string is in the dictionary.
"""""

# file= open('words.txt','r')
# rd=file.read()
# words=rd.split(' ')

# #print words

# for word in words:
#     #d=words
#     print(word)

# file= open('words.txt','r')
# d=dict()

# for line in file:
#     words=line.split()
#     for word in words:
#         if word not in d:
#             d[word]=1
#         else:
#             d[word]=2

# print(d)

# #looping through a dictionary
# counts={'chucks':1,'annie':3,'jan':100}

# for keys in counts:
#     print(keys,counts[keys])


# counts={'chucks':1,'annie':31,'jan':100}
# for keys in counts:
#     if counts[keys]>10:
#         print((keys),counts[keys])

#sorting by keys
counts={'chucks':1,'annie':31,'jan':100}
#convert to list
lst=list(counts.keys())
lst.sort()
for n in lst:
    print(n,counts[n])

#sorting by value
counts={'chucks':1,'annie':31,'jan':100}
lst=list(counts.values())
lst.sort()
for n in lst:
    print(n)

#tex