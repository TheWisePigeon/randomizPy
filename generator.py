from faker import Faker
fake = Faker()

def generator(schema, rows):
    print(dir(fake)) 
    generated = []
    for i in range(rows):
        for field in schema:
            print(field)
            generatedData =  fake.name()
            print(generatedData)
    