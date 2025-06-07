keys = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
values = [1, 2, 2, 3]
d = {}
for k, v in zip(keys, values):
    d[k] = {v}
print(d)