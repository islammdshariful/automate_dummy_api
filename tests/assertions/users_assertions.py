from assertpy import assert_that
from cerberus import validator


def assert_users_have_user_with_email(response, email):
    assert_that(response.as_dict).extracting('email').is_not_empty().contains(email)


def assert_users_have_user_with_username(response, username):
    assert_that(response.as_dict).extracting('username').is_not_empty().contains(username)


def assert_user_is_present(is_new_user_created):
    assert_that(is_new_user_created).is_not_empty()
