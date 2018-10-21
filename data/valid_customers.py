from model.customer import Customer
from generators import generators

valid_customers = [Customer(firstname=generators.name(), lastname=generators.name(), address=generators.address(),
                        postcode=generators.postcode(), city=generators.name(), country="united states",
                        zone='AL', email=generators.email(), password=generators.password(), phone=generators.phone())]

