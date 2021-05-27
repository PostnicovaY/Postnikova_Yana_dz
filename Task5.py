src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []

for el in src:
    if el in result:
        result.remove(el)
        src = [i for i in src if i != el]
    else:
        result.append(el)

print(result)