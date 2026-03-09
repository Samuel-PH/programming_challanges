#Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.\

def print_name_proper_casing():
    full_name = input("Please enter your full name: ")
    proper_name = full_name.title()
    
    print(proper_name)

print_name_proper_casing()