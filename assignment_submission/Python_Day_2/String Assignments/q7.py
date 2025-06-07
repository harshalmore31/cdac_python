def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet.issubset(set(sentence.lower()))

text = input("Enter a sentence: ")

if is_pangram(text):
    print("It is a pangram")
else:
    print("It is not a pangram")