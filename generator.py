from faker import Faker
fake = Faker()
from generators import generators as gens

def generator(schema, rows):
    generated = []
    for i in range(rows):
        for field in schema:
            print(field)
            generatedData =  fake.name()
            print(generatedData)
    

