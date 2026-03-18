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


#Optimized
def manual_isupper():
    text = input("Text: ")
    has_upper = False
    
    for c in text:
        if 'a' <= c <= 'z': return print("Result: False")
        if 'A' <= c <= 'Z': has_upper = True
        
    print(f"Result: {has_upper}")

manual_isupper()

#STEPS:
#1. Get input from the user for the text.
#2. Define the lowercase and uppercase alphabets.
#3. Iterate through each character in the input text.
#4. If a character is found in the lowercase alphabet, print "Result: False" and return.
#5. If a character is found in the uppercase alphabet, set a flag to indicate that an uppercase character has been found.
#6. After the loop, print "Result: True" if an uppercase character was found, otherwise print "Result: False".
