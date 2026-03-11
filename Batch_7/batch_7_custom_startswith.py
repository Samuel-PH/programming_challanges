#startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

def manual_startswith():
    user_input = input("Please enter your text: ")
    prefix = input("Please enter the prefix to check: ")

    if len(prefix) > len(user_input):
        print("result: False")
        return

    is_starting_with_prefix = True
    for i in range(len(prefix)):
        if user_input[i] != prefix[i]:
            is_starting_with_prefix = False
            break

    print(f"result: {is_starting_with_prefix}")

manual_startswith()