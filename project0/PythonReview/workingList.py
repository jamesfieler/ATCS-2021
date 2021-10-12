careers = ['programmer', 'biologist', 'teacher', 'engineer']

print(careers[1])
print('biologist' in careers)
careers.append('artist')
careers.insert(0, 'actor')
for i in range(len(careers)):
    print(careers[i])