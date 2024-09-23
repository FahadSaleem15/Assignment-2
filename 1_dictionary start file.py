import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print(phonebook)

print(len(phonebook))

mydict = dict(m=8, n=9)

print(mydict)

print(phonebook['Chris'])



print()
print('*****  end section 1 ********')
print()




print()
print('*****  start section 2 - search dictionary ********')
print()


name = 'Chris'

if name in phonebook:
    print(phonebook[name])
else:
    print(f"{name} is not in the phonebook")




print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

phonebook['Joe'] = '555-0123'

phonebook['Chris'] = '555-4444'

print(phonebook)


print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

del phonebook['Chris']

print(phonebook)


print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()


for key in phonebook:
    print(f"name: {key} and phone number: {phonebook[key]}")

for v in phonebook.values():
    print(v)

for k,v in phonebook.items():
    print(f"The key is {k} and the value is {v}")

for my_tuple in phonebook.items():
    print(f"{my_tuple}")

print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()


phone = phonebook.get('Chris', 'Key not found')
print(phone)

phonebook.clear()

print(phonebook)



print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

remove = phonebook.pop('Chris', 'Key not found')
print(remove)
print(phonebook)


print()
print('*****  end section 7 ********')
print()




print()
print('*****  start section 8 - using popitem ********')
print()

a = phonebook.popitem()
print(a)
print(phonebook)




print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

import random
print(f"The key is {random.choice(list(phonebook))} and the value is {phonebook[random.choice(list(phonebook))]}")



print()
print('*****  end section 9 ********')
print()