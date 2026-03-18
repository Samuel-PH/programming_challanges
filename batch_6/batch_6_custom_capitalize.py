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

#Optimized

def manual_capitalize():
    text = input("Please enter your text: ")
    print(f"Result: {text[:1].upper() + text[1:].lower()}")

manual_capitalize()

#STEPS:
#1. Take input from the user.
#2. Check if the input is empty. If it is, print "Result: " and return.
#3. Get the first character of the input and convert it to uppercase.  
#4. Get the rest of the text (from the second character to the end) and convert it to lowercase.
#5. Add both parts together and print the result.
