#upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

def manual_upper():
    user_input = input("Please enter your text: ")
    upper_text = ""

    for char in user_input:
        if 'a' <= char <= 'z':
            upper_char = chr(ord(char) - (ord('a') - ord('A')))
            upper_text += upper_char
        else:
            upper_text += char

    print(f"result: '{upper_text}'")

manual_upper()