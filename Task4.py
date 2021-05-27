src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

def gen(src):
    for i in range(1, len(src)):
        if src[i]>src[i-1]:
            yield src[i]
        else:
            yield None

extractor = gen(src)
result = []
for i in range(1, len(src)):
    el = next(extractor)
    if not (el is None):
        result.append(el)
print(result)