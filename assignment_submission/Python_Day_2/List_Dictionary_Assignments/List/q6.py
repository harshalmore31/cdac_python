colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
result = [colors[i] for i in range(len(colors)) if i not in [0, 4, 5]]
print(result)