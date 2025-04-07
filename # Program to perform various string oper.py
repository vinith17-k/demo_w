# Program to perform various string operations without built-in functions

# 1. Calculate Length of String
def string_length(s):
    count = 0
    for i in s:
        count += 1
    return count

# 2. String Reversal
def reverse_string(s):
    rev = ""
    for i in s:
        rev = i + rev
    return rev

# 3. Equality Check of Two Strings
def check_equality(s1, s2):
    if string_length(s1) != string_length(s2):
        return False
    for i in range(string_length(s1)):
        if s1[i] != s2[i]:
            return False
    return True

# 4. Check Palindrome
def check_palindrome(s):
    if s == reverse_string(s):
        return True
    else:
        return False

# 5. Check Substring
def check_substring(s, sub):
    len_s = string_length(s)
    len_sub = string_length(sub)

    for i in range(len_s - len_sub + 1):
        match = True
        for j in range(len_sub):
            if s[i + j] != sub[j]:
                match = False
                break
        if match:
            return True
    return False


# Main Program
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
substring = input("Enter substring to check: ")

print("Length of first string:", string_length(string1))
print("Reverse of first string:", reverse_string(string1))

if check_equality(string1, string2):
    print("Both strings are Equal.")
else:
    print("Strings are Not Equal.")

if check_palindrome(string1):
    print("First string is a Palindrome.")
else:
    print("First string is Not a Palindrome.")

if check_substring(string1, substring):
    print("Substring Found in first string.")
else:
    print("Substring Not Found in first string.")

print("Name: Abhijeet Ingale")
print("Roll No: 1721")
