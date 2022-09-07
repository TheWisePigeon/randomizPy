from faker import Faker
fake = Faker()
from generators import generators as gens

def generator(schema, rows):
    generated = {}
    generatedRows=[]
    for i in range(rows):
        row = {}
        for field in schema:
            for generator in gens:
                if generator['alias']==schema[field]:
                    row[f"{field}"] = generator['generator']()
        generated[f"{i}"] = row
    return generated