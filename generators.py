from faker import Faker
fake = Faker()

print(dir(fake))


generators = [
    {
        "alias": "name",
        "generator": fake.name
    },
    {
        "alias": "email",
        "generator": fake.email
    },
    {
        "alias": "address",
        "generator": fake.address
    },
    {
        "alias": "date",
        "generator": fake.date
    }
]

print(generators) 