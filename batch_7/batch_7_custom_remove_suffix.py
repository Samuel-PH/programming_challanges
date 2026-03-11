#removesuffix() remove the characters at the end of the string that matches the function parameter. 
#Create a program that do the same functionality without using removesuffix() function.

def manual_removesuffix():
    main_text = input("Please enter your main text: ")
    suffix = input("Please enter the suffix to remove: ")
    suffixlength = len(suffix)

    if suffixlength == 0:
        result = main_text
        
    elif main_text[-suffixlength:] == suffix:
        result = main_text[:-suffixlength]
        
    else:
        result = main_text
    print(f"Result: '{result}'")

manual_removesuffix()
