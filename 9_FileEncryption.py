
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ','.',':']


special_charcs = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
    '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', 'P', 'A', '<', '>', 
    '/', '?', 'K', '~', 'Q', 'N', 'O', 'J', 'H', 'F', 'C', 'L', 'B', 
    'Z', 'V', 'H', 'J', 'I', 'T', 'S', 'W', 'U', 'M', 'V', ' ', '.', ':']






file = open("info_security-1.txt", "r")
reader = file.read()

codes = {}

for i in range(len(letters)):
    codes[letters[i]] = special_charcs[i]


print(codes)

new_charc = ""
for letter in reader:
    new_charc += codes[letter]


new_file = open('encrypted.txt','w')

new_file.write(new_charc)

new_file.close()





