#count() return how many time the function parameter appear in the string. 
#Create a program that do the same functionality without using count() function. (make sure to count the character in the string and return the result also make it be able to count words in the string)

def manual_count():
    user_input = input("Please enter your text: ")
    search_term = input("Please enter the character or word to count: ")

    count = 0
    for i in range(len(user_input)):
        if user_input[i:i+len(search_term)] == search_term:
            count += 1

    print(f"The term '{search_term}' appears {count} times in the text.")  

manual_count()  