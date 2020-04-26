number = [5, 8, 13, 24, 7, 16]
name = ['bass', 'kimhun5', 'meen']
mixed = ['bass', 2, 4, 'ok']


print(number[1])
print(mixed)

# count member list
print(len(name))

# empty list
data = []
# add list empty
data.append(1)
data.append(151)
data.append("bass")

print(data)
# update value list
data[1] = 12
print(data)


# loop
for val in data:
    print(val)


sum = 0
for num in number:
    sum += num

print(sum)
