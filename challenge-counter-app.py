# Basic Data Types Challenge 1: Letter Counter App

print("Welcome to the Letter Counter App")

# Get user input
name = input("\nWhat's your name: ").title().strip()
print("Hello, " + name + "!")

print("I'll count the number of times that a specific letter occurs in a message.")
message = input("\nPlease enter a message: ")
letter = input("Which letter would you like to count the occrrences of: ")

# Standardize
message = message.lower()
letter = letter.lower()

# Get the count and display results
letter_count = message.count(letter)
print("\n" + name + ", your message has " + str(letter_count) + " character '" + letter + "' in it.")