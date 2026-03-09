# Create a program that ask the user to input their fullname. Print the input in all capital letter.

def print_name_uppercase():
    full_name = input("Please enter your full name: ")
    uppercase_name = full_name.upper()

    print(uppercase_name)

print_name_uppercase()