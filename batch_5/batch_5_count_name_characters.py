#Create a program that ask the user to input their fullname. Print the number of characters in the input.

def count_name_characters():
    full_name = input("Please enter your full name: ")
    character_count = len(full_name)

    print(f"Total number of characters: {character_count}")

count_name_characters()