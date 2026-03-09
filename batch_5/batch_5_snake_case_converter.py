#Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

def convert_to_snake_case():
    full_name = input("Please enter your full name: ")
    snake_case_name = full_name.lower().replace(" ", "_")

    print(snake_case_name)

convert_to_snake_case()