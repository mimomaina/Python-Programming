#store product information
#create dictionary
user_dict ={}


users_input =input('Enter name,price,quantity')
for users_input in user_dict:
    key=('Enter the key:')
    value=('Enter the value:')
    user_dict[key]=value


def update_item():
    key = input("Enter the key you want to update: ")
    if key in user_dict:
        value = get_value()  
        user_dict[key] = value
        print(f"Updated {key} to {value}")
    else:
        print(f"Key '{key}' not found in the dictionary.")

print(user_dict)

def remove_item():
    key = input("Enter the key you want to remove: ")
    if key in user_dict:
        del user_dict[key]  # Remove key-value pair from dictionary
        print(f"Removed {key} from the dictionary.")
    else:
        print(f"Key '{key}' not found in the dictionary.")



