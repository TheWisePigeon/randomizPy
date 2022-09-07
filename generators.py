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
    },
    {
        "alias": "bool",
        "generator": fake.boolean
    },
    {
        "alias": "city",
        "generator": fake.city
    },
    {
        "alias": "color",
        "generator": fake.color
    },
    {
        "alias": "country",
        "generator": fake.country
    },
    {
        "alias": "date",
        "generator": fake.date
    },
]

print(generators) 