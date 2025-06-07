d = {
    'Names': ['Rohit', 'Ganesh', 'SRK', 'Akshay'],
    'age': 40,
    'addresses': ['Mumbai', 'Delhi', 'Kolkara', 'Banglore'],
    'emails': ['actor.gmail.com', 'movie.gmail.com']
}
count = sum(len(v) for v in d.values() if isinstance(v, list))
print(count)  # 10