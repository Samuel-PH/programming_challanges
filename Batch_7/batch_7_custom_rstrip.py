#rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

def manual_rstrip():
    user_input = input("Please enter your text: ")
    end_index = len(user_input) - 1

    while end_index >= 0 and user_input[end_index] == " ":
        end_index = end_index - 1
    clean_text = user_input[:end_index + 1]
    
    print(f"Cleaned output: '{clean_text}'")

manual_rstrip()
