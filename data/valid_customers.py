from model.customer import Customer
from conftest import app

valid_customers = [Customer(firstname=app.generate.name(), lastname=app.generate.name(), address=app.generate.address(),
                        postcode=app.generate.postcode(), city=app.generate.name(), country="united states",
                        zone='AL', email=app.generate.email(), password=app.generate.password())]

