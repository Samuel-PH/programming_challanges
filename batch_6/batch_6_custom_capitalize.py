#capitalize() makes the first letter of the string, capital letter. And all other letter in small case.
#Create a program that do the same functionality without using capitalize() function.

def manual_capitalize():
    user_input = input("Please enter your text: ")

    if len(user_input) == 0:
        print("Result: ")
        return 

    first_character = user_input[0].upper()
    rest_of_text = user_input[1:].lower()
    capitalized_text = first_character + rest_of_text

    print(f"Result: {capitalized_text}")

manual_capitalize()