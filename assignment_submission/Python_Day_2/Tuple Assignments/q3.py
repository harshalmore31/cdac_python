mytuple = (1, 2, 3, 2, 4, 5, 1, 6, 3)

repeats = set()
for item in mytuple:
    if mytuple.count(item) > 1:
        repeats.add(item)

print("Repeated Items:", repeats)