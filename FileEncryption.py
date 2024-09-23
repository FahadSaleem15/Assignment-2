import random
import string


special_characters = string.punctuation
list_of_characters = list(special_characters)

codes = {}


file = open("info_security-1.txt", "r")
reader = file.read()


while len(list_of_characters) < len(reader):
    list_of_characters += list_of_characters

for i in range(len(reader)):
    codes[reader[i]] = list_of_characters[i]

print(codes)

new_charc = ""
for letter in reader:
    new_charc += codes[letter]


with open("encrypted.txt", 'w') as file:
    file.write(new_charc)

file.close()


