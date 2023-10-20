# import modules

import pytest

# from app import create_app, db # put in conftest.py ??
from app.models.user import User

def test_it_exists_with_attributes():
    user_data = {
        "email": "test@email.com",
        "password": "PLAIN_TEXT_PASSWORD",
        "phone_number": "1234567890",
        "first_name": "Namey",
        "last_name": "McNameface"
    }

    user_instance = User(**user_data)

    assert user_instance.email == user_data.email
    assert user_instance.password != user_data.password
    assert user_instance.phone_number == user_data.phone_number
    assert user_instance.first_name == user_data.first_name
    assert user_instance.last_name == user_data.last_name
