#rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. 
#Create a program that do the same functionality without using rjust() function.

def manual_rjust():
    user_input = input("Please enter your text: ")
    total_length = int(input("Please enter the total length for rjust: "))

    if total_length <= len(user_input):
        print(f"result: '{user_input}'")
        return

    spaces_needed = total_length - len(user_input)
    justified_text = ' ' * spaces_needed + user_input

    print(f"result: '{justified_text}'")

manual_rjust()
