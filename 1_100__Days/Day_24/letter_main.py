place_holder = "[name]"

with open('name.txt') as f:
    names = f.readlines()

with open('invitation_letter.txt') as f:
    letter_content = f.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(place_holder, stripped_name)

        filename = f"letter_for_{stripped_name}.txt"

        with open(filename, 'w') as f:
            f.write(new_letter)

        