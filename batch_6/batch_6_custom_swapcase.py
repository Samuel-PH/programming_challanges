#swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

def manual_swapcase():
    user_input = input("Please enter your text: ")
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz" 
    swapped_text = ""
    
    for char in user_input:
        
        if char in upper_alphabet:
            position = upper_alphabet.index(char)
            swapped_text += lower_alphabet[position]

        elif char in lower_alphabet:
            position = lower_alphabet.index(char)
            swapped_text += upper_alphabet[position]

        else:
            swapped_text += char
            
    print(f"Result: {swapped_text}")

manual_swapcase()