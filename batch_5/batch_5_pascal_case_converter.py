def convert_to_pascal_case():
    full_name = input("Please enter your full name: ")
    pascal_case_name = full_name.title().replace(" ", "")

    print(pascal_case_name)

convert_to_pascal_case()