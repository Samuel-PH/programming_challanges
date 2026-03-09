#endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function../

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