# import re

# string='Hello world'
# pattern=(r'^H')
# match= re.search(pattern,string)
# if match:
#     # print('word found')
#     #OR
#     print('found',match.group())
# else:
#     print('No match')

#Basic RegEx
"""""
. - matches any single character expect new line
d- matches any digital character(0-9)
w-matches any word character (a-z,A-Z,0-9,_)\\a letter or digit or underbar
b- boundaries between words and non words
s-matches any whitespaces(tab(\b),newline(//),return(\r),space\f)
^-start of a string
$-end of a string
\\ - match backslash\
\. - match fullstop
+  - matches one or more occurence of the psttern to its left
*  - matches zero or more occurence of the pattern to its left
?  - matches zero or one occurence ofthe pattern to its left

                              
"""""
#Example 1
#import re
# string='p12358g'
# pattern =r'\d\d\d\d\d'
# match =re.search (pattern,string)

# if match:
#     print(match.group())
# else:
#     print('not found')

# import re
# string='123-456-7890'
# pattern =r'\d\d\d\-\d\d\d\-\d\d\d\d'
#or 
# pattern= r'\d{3}-\d{3}-\d{4}'
# match =re.search (pattern,string)

# if match:
#     print(match.group())
# else:
#     print('not found')



# import re
# string= 'piling'
# pattern= r'..g'
# match =re.search (pattern,string)
#output ing
# if match:
#     print(match.group())
# else:
#     print('not found')

# import re
# string = 'piiing'
# pattern=r'pii+'
# match=re.search(pattern,string)

# if match:
#     print(match.group())
# #output:piii
# else:
#     print('not found')


#zero or more white spaces
# import re
# string = 'xx1 2  3xx'
# pattern=r'\d\s*\d\s*\d'
# match=re.search(pattern,string)

# if match:
#     print(match.group())
# #output:1 2 3
# else:
#     print('not found')


# import re
# string = 'foobar'
# pattern=r'^b\w+'
# match=re.search(pattern,string)

# if match:
#     print(match.group())
# # #output:starts with b
# else:
#     print('not found')


#finding email

import re
string = 'purple alice-b@google.com monkey dishwasher'
#pattern=r'\w+@\w+\.\w+'
pattern=r'[\w.]+@[\w.-]+'
match=re.search(pattern,string)

if match:
    print(match.group())
#output:b@google.com
else:
    print('not found')

# import re
# string = 'purple alice-b@google.com monkey dishwasher'

# pattern=r'[\w.-]+@[\w.-]+'
# match=re.search(pattern,string)

# if match:
#     print(match.group())
# # #output:b@google.com
# else:
#     print('not found')