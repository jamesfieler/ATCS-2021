firstName = 'james'
print(firstName)

print(firstName.capitalize())

capName = ''
for i in range(len(firstName)):
    capName += firstName[i].capitalize()
print(capName)