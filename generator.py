from faker import Faker

def generator(schema, rows):
    for i in range(rows):
        for field in schema:
            print(field)
    