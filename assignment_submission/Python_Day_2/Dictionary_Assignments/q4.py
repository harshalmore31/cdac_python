# 4)  Given a dictionary of students and their favourite colours: 
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'} 
# 1. Find out how many students are in the list 
# 2. Change Lisa’s favourite colour 
# 3. Remove 'Jenny' and her favourite color
# 4. Sort and print students and their favourite colours alphabetically by name


people = {'Arham': 'Blue', 'Lisa': 'Yellow', 'Vinod': 'Purple', 'Jenny': 'Pink'}
print("Original dictionary:", people)

# 1. Find out how many students are in the list
num_students = len(people)
print("1. Number of students:", num_students)

# 2. Change Lisa’s favourite colour
new_color_lisa = input("Enter Lisa's new favourite color: ") # e.g. Green
people['Lisa'] = new_color_lisa
print("2. After changing Lisa's color:", people)

# 3. Remove 'Jenny' and her favourite color
if 'Jenny' in people:
    del people['Jenny']
print("3. After removing Jenny:", people)

# 4. Sort and print students and their favourite colours alphabetically by name
print("4. Sorted students and their favourite colours:")

# To sort by name (key), we get the keys, sort them, then iterate
sorted_names = sorted(people.keys())
for name in sorted_names:
    print(f"{name}: {people[name]}")
print("-" * 20)