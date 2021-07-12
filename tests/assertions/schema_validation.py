from assertpy import assert_that, soft_assertions

from ..data.schema_sample import user_schema
from cerberus import Validator


def for_one_user(user):
    validator = Validator(user_schema, require_all=True)
    is_valid = validator.validate(user)
    with soft_assertions():
        assert_that(is_valid, description=validator.errors).is_true()


def for_multiple_users(users):
    validator = Validator(user_schema, require_all=True)
    with soft_assertions():
        for person in users:
            is_valid = validator.validate(person)
            assert_that(is_valid, description=validator.errors).is_true()
