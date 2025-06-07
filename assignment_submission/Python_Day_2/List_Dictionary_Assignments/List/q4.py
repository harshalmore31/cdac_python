words = ['abc', 'xyz', 'aba', '1221']
result = [word for word in words if len(word) >= 2 and word[0] == word[-1]]
print("Matching strings:", result)