#Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.

def swap_name_casing():
    full_name = input("Please enter your full name: ")
    reversed_casing_name = full_name.swapcase()
    
    print(reversed_casing_name)

swap_name_casing()