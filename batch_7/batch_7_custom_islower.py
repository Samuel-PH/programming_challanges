#islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

def manual_islower():
    user_input = input("Please enter your text: ")
    is_lower = True

    for char in user_input:
        if 'A' <= char <= 'Z':
            is_lower = False
            break

    print(f"result: {is_lower}")

manual_islower()