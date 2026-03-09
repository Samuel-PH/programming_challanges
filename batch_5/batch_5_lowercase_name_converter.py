#Create a program that ask the user to input their fullname. Print the input in all lower case.

def print_name_lowercase():
    full_name = input("Please enter your full name: ")
    lowercase_name = full_name.lower()
    
    print(lowercase_name)

print_name_lowercase()