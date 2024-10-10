# Open the file in read mode
with open('sample.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Print each line separately
        print(line.strip())  