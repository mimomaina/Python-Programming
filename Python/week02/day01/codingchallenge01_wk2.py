#Length of a sentence
# text= input("Enter a sentence")
# text_length=len(text)
# print(len(f"The length of the entered sentence is: {text_length}"))


# word1 = input("Enter the first word: ")
# word2 = input("Enter the second word: ")

# # remove spaces and convert to lowercase
# word1 = word1.replace(" ", "").lower()
# word2 = word2.replace(" ", "").lower()

# # Check if the words are anagrams by sorting both words and comparing
# if sorted(word1) == sorted(word2):
#     print(f'"{word1}" and "{word2}" are anagrams.')
# else:
#     print(f'"{word1}" and "{word2}" are not anagrams.')

# palindrome
# word = input("Enter a word or phrase: ")

# # Remove spaces and convert to lowercase 
# processed_word = word.replace(" ", "").lower()

# # Check if the cleaned word is the same forwards and backwards
# if processed_word ==processed_word[::-1]:
#     print(f'"{word}" is a palindrome.')
# else:
#     print(f'"{word}" is not a palindrome.')


# Open the existing file 
with open('mbox.txt', 'r') as source_file:

    content = source_file.read()

with open('ruth.txt', 'w') as target_file:

    target_file.write(content)

print("Content copied successfully to the new file.")

# Open the file in read mode
with open('mbox.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Print each line separately
        print(line.strip())  
