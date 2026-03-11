#index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

def manual_index():
    user_input = input("Please enter your text: ")
    search_term = input("Please enter the character or word to find: ")

    index = -1
    for i in range(len(user_input) - len(search_term) + 1):
        if user_input[i:i+len(search_term)] == search_term:
            index = i
            break

    if index != -1:
        print(f"The term '{search_term}' is found at index {index}.")
    else:
        print(f"The term '{search_term}' is not found in the text.")

manual_index()