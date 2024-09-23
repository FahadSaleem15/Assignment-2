import string

file_alpha = open("info_security-1.txt","r")

file_speccharc = open("encrypted.txt","r")



alpha_reader = file_alpha.read()
speccharc_reader = file_speccharc.read()


char_to_special = {alpha_reader[i]: speccharc_reader[i] for i in range(len(alpha_reader))}

special_to_char = {v: k for k, v in char_to_special.items()}



new_text = ""
for char in speccharc_reader:
        new_text += special_to_char.get(char, char)


print(new_text)


