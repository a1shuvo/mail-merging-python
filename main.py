with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()


for name in names:
    stripped_name = name.strip()
    new_letter = letter.replace("[name]", stripped_name)
    with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as output:
        output.write(new_letter)
