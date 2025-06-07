x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
for k in y:
    if k in x and x[k] == y[k]:
        print(f"{k}: {x[k]} is present in both x and y")