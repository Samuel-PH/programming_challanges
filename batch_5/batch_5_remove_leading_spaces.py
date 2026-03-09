#Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

def remove_leading_spaces():
    full_name = input("Please enter your full name: ")
    
    clean_name = full_name.lstrip()
    
    print(clean_name)

remove_leading_spaces()