Frequency = {}

text = open("sometext.txt","r")

content = text.read()

list = content.split()


for word in list:
    Frequency[word] = list.count(word)

print(Frequency)