import pytest
from data.valid_customers import valid_customers


@pytest.mark.parametrize("customer", valid_customers, ids=[repr(x) for x in valid_customers])
def test_user_registration(app, customer):
    app.session.open_litecart()
    app.litecart.create_new_customer(customer)
    app.litecart.customer_logout()
    app.litecart.customer_login(customer)
    app.litecart.customer_logout()




