# Program to count occurrences of a character in a string without using built-in functions

# Input string from user
string = input("Enter a string: ")

# Input character to be counted
char = input("Enter a character to count: ")

# Initialize count variable
count = 0

# Loop through each character in string
for i in string:
    if i == char:
        count += 1

# Output
print("The character", char, "occurs", count, "times in the string.")

# Name and Roll No.
print("Name: Abhijeet Ingale")
print("Roll No: 1721")
