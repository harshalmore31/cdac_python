text = input("Enter a string: ")

repeats = set()
for char in text:
    if text.count(char) > 1:
        repeats.add(char)

print("Repeated characters:", repeats)