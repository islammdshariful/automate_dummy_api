import logging
import random
import sys

import pytest
from pytest_reportportal import RPLogger, RPLogHandler

from ..utils.file_reader import read_file


@pytest.fixture
def create_data():
    payload = read_file('create_person.json')

    random_no = random.randint(0, 1000)
    last_name = f'Olabini{random_no}'

    payload['lname'] = last_name
    yield payload