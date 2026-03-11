#zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. 
#Create a program that do the same functionality without using zfill() function.

def manual_zfill():
    user_input = input("Please enter your text: ")
    total_length = int(input("Please enter the total length for zfill: "))

    if total_length <= len(user_input):
        print(f"result: '{user_input}'")
        return

    zeros_needed = total_length - len(user_input)
    filled_text = '0' * zeros_needed + user_input

    print(f"result: '{filled_text}'")  

manual_zfill()
