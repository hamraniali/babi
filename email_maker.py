from faker import Faker

faker = Faker()
print(faker.email())

for i in range(2000):
    email = faker.email()
    if "@gmail.com" in email:
        if i % 2 == 0:
            print(email.replace('@gmail.com', '@stu.yazd.ac.ir'))
        else:
            print(email)