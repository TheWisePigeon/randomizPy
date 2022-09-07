from faker import Faker
fake = Faker()

generators = [
    {
        "alias": "name",
        "generator": fake.name()
    },
    {
        "alias": "email",
        "generator": fake.email()
    },
]