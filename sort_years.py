users = [
    {"name": "Анна", "age": 25},
    {"name": "Борис", "age": 19},
    {"name": "Вика", "age": 30}
]

sorted_users = sorted(users, key=lambda user: (len(user['name']), user['name']))
print(sorted_users)