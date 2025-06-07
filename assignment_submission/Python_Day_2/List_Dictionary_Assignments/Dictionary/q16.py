Students = {'d 01': 'Abc', 'd 0 2': 'Xyz', 'd0 3': 'Pqr'}
cleaned = {k.replace(' ', ''): v for k, v in Students.items()}
print(cleaned)