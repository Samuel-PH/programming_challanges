#Create a program that ask the user to input a complete statement. Print the number of words in the input.

def count_words_in_statement():
    user_statement = input("Please enter a complete statement: ")
    words_list = user_statement.split()
    word_count = len(words_list)

    print(f"Number of words: {word_count}")

count_words_in_statement()