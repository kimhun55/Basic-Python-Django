# dictionnary เก็บเป็น key->value json
scores = {
    'bass': 1220,
    'k': 12312,
    'b': 8596
}

print(scores)
print(scores['b'])

scores['roger'] = True

print(scores)


# dictionnary emty
points = {}
points['m'] = 12
points['b'] = "dsf"

print(points)

# loop
for k, v in scores.items():
    print(k, v)
