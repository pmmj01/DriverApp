import os
import sys
import pytest
from django.test import Client
from .testutils import *

sys.path.append(os.path.dirname(__file__))

@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def set_up():
    for _ in range(10):
        create_fake_user()
    for _ in range(10):
        create_fake_address_company_from()
    for _ in range(10):
        create_fake_address_company_to()
    for _ in range(20):
        create_fake_trailer()
    for _ in range(20):
        create_fake_car()
