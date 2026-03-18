#endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

def check_ends_with_manual():
    main_text = input("Please enter the main text: ")
    suffix = input("Please enter the suffix to check: ")
    main_length = len(main_text)
    suffix_length = len(suffix)

    if suffix_length > main_length:
        print("Result: False")

    elif suffix_length == 0:
        print("Result: True")

    else:
        start_position = main_length - suffix_length
        end_chunk = main_text[start_position:]

        if end_chunk == suffix:
            print("Result: True")
        else:
            print("Result: False")

check_ends_with_manual()

#Optimized

def check_ends_with_manual():
    text = input("main text: ")
    suffix = input("suffix: ")
    print(f"Result: {text[len(text) - len(suffix):] == suffix}")

check_ends_with_manual()

#STEPS:
#1. Get input from the user for the main text and the suffix to check.
#2. Calculate the length of the main text and the suffix.
#3. If the suffix length is greater than the main text length, print "Result: False".
#4. If the suffix length is zero, print "Result: True".
#5. Otherwise, calculate the starting position for the end chunk of the main text and compare it with the suffix. Print "Result: True" if they match, otherwise print "Result: False".