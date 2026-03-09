#title() makes all first letter of each word in the string, capital letter. And all other letter in small case. 
#Create a program that do the same functionality without using title() function.

def manual_title_case():
    user_input = input("Please enter your text: ")
    title_case_text = ""
    is_new_word = True

    for char in user_input:
        if is_new_word:
            title_case_text += char.upper()
            is_new_word = False

        else:
            title_case_text += char.lower()

        if char == " ":
            is_new_word = True
            
    print(f"Result: {title_case_text}")

manual_title_case()