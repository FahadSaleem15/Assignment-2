special_charcs = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
    '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', 'P', 'A', '<', '>', 
    '/', '?', 'K', '~', 'Q', 'N', 'O', 'J', 'H', 'F', 'C', 'L', 'B', 
    'Z', 'V', 'H', 'J', 'I', 'T', 'S', 'W', 'U', 'M', 'V', ' ', '.', ':']


letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ','.',':']

charc_file = open('encrypted.txt', 'r')

charc_reader = charc_file.read()

alph = {}

for i in range(len(special_charcs)):
    alph[special_charcs[i]] = letters[i]

print(alph)

updated_letters = ""
for charc in charc_reader:
    updated_letters += alph[charc]

print(updated_letters)


