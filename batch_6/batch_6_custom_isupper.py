#isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

def check_is_upper_manual():
    user_input = input("Please enter your text: ")
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    found_uppercase = False
    
    for char in user_input:
        if char in lower_alphabet:
            print("Result: False")
            return 
            
        elif char in upper_alphabet:
            found_uppercase = True

    print(f"Result: {found_uppercase}")

check_is_upper_manual()    