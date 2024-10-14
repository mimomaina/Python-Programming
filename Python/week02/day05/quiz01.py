import re

def check_string(s):
    pattern = r'^[a-zA-Z0-9]+$'
    
    if re.match(pattern, s):
        return True
    else:
        return False

test_string = "Hello123"
if check_string(test_string):
    print("The string contains only a-z, A-Z, or 0-9 characters.")
else:
    print("The string contains other characters.")
