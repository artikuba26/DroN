import json

file = open('accounts.txt', 'r+', encoding='Latin-1')
users = json.load(file)

for user in users:
    print(user)



file.close()