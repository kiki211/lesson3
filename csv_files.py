import csv

# with open('users.csv', 'r', encoding='utf-8') as f:
#     fields = ['first_name', 'last_name', 'email', 'gender', 'balance']
#     reader = csv.DictReader(f, fields, delimiter=';')
#     for row in reader:
#         print(row)
#
# user_list = []
# with open('export.csv', 'w', encoding='utf-8', newline='') as f:
#     fields = ['first_name', 'last_name', 'email', 'gender', 'balance']
#     writer = csv.DictWriter(f, fields, delimiter=';')
#     writer.writeheader()
#     for user in user_list:
#         writer.writerow(user)


# Task 1
friends = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'}
        ]

with open('my_friends.csv', 'w', encoding='utf-8', newline='') as file:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(file, fields, delimiter =',')
    writer.writeheader()
    for friend in friends:
        writer.writerow(friend)