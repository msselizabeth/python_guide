from faker import Faker
import json
fake = Faker("en_CA")

filename = input("Enter a filename.format >>> ")
amount = int(input("How many fake users you need >>> "))

def get_user():
    user = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
    }
    return user

users = []

for i in range(amount):
    users.append(get_user())

print(users)

with open(filename, 'w') as file:
    json.dump(users, file, indent=4)
    # file.write(str(users))