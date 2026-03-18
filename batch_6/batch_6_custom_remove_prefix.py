# removeprefix() remove the characters at the beginning of the string that matches the function parameter. 
# Create a program that do the same functionality without using removeprefix() function.

def remove_custom_prefix():
    main_text = input("Please enter the main text: ")
    prefix = input("Please enter the prefix to remove: ")

    prefix_length = len(prefix)
    if main_text[:prefix_length] == prefix:
        result = main_text[prefix_length:]
    else:
        result = main_text
        
    print(f"Result: {result}")

remove_custom_prefix()

#Optimized

def manual_removeprefix():
    text = input("Text: ")
    prefix = input("Prefix: ")
    print(f"Result: {text[len(prefix):] if text[:len(prefix)] == prefix else text}")

manual_removeprefix()
