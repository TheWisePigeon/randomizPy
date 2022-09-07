from faker import Faker
fake = Faker()
from generators import generators as gens

def generator(schema, rows):
    generated = []
    for i in range(rows):
        for field in schema:
            for generator in gens:
                if generator['alias']==schema[field]:
                    print(generator['generator']())
    

