#lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

def remove_leading_spaces_manual():
    user_input = input("Please enter your text: ")
    start_index = 0

    while start_index < len(user_input) and user_input[start_index] == " ":
        start_index = start_index + 1
        
    clean_text = user_input[start_index:]

    print(f"Cleaned output: [{clean_text}]")

remove_leading_spaces_manual()

#Optimized

def manual_lstrip():
    text = input("Text: ")
    while text[:1] == ' ': text = text[1:]
    print(f"Result: [{text}]")

manual_lstrip()
