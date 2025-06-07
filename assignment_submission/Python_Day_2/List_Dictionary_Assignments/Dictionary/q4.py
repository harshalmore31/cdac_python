data = [{'id': 1, 'success': True}, {'id': 2, 'success': False}, {'id': 3, 'success': True}]
count = sum(1 for d in data if d['success'])
print(count)