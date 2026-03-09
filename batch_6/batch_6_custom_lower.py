#lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

def lowercase_converter():
    user_input = input("Please enter your text: ")
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    lowercased_text = ""
    
    for char in user_input:
        if char in upper_alphabet:
            position = upper_alphabet.index(char)
            lowercased_text += lower_alphabet[position]
            
        else:
            lowercased_text += char
            
    print(f"Result: {lowercased_text}")

lowercase_converter()