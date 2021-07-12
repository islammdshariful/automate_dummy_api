import json
from json import dumps

import requests

from clients.users.people_client import UserClient
from tests.assertions.users_assertions import *
from tests.assertions.schema_validation import *
from tests.helpers.people_helpers import *
from utils.print_helpers import pretty_print

client = UserClient()


def test_read_all_has_user():
    response = client.read_all_users()
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_users_have_user_with_email(response, email='Chaim_McDermott@dana.io')


def test_new_user_can_be_added():
    username, response = client.create_user()
    assert_that(response.status_code, description='User not created').is_equal_to(requests.codes.no_content)

    users = client.read_all_users().as_dict
    is_new_user_created = search_created_user_in(users, username)
    assert_user_is_present(is_new_user_created)


def test_created_user_can_be_deleted():
    user_username, _ = client.create_user()
    pretty_print(user_username)

    peoples = client.read_all_users().as_dict
    new_user_id = search_created_user_in(peoples, user_username)['id']
    print(new_user_id)

    response = client.delete_user(new_user_id)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)


def test_get_all_users():
    response = client.read_all_users()
    pretty_print(response.as_dict)


def test_get_specific_user():
    user_id = 7
    response = client.read_one_user_by_id(user_id)
    pretty_print(response.as_dict)


def test_delete_specific_user():
    user_id = 12
    response = client.delete_user(user_id)
    pretty_print(response.as_dict)


def test_update_specific_user():
    payload = dumps({
        "street": "10",
        "suite": "Avenue 12",
        "city": "Dhaka"
    })
    user_id = 2
    client.update_user(user_id, payload=payload)

    response = client.read_one_user_by_id(user_id)
    pretty_print(response.as_dict)


def test_user_can_be_added_with_a_json_template(create_data):
    client.create_user(create_data)

    response = client.read_all_users()
    users = response.as_dict

    result = search_nodes_using_json_path(users, json_path="$.[*].username")

    expected_username = create_data['username']
    assert_that(result).contains(expected_username)


def test_read_one_operation_has_expected_schema():
    user_id = 1
    response = client.read_one_user_by_id(user_id)
    user = json.loads(response.text)

    for_one_user(user)


def test_read_all_operation_has_expected_schema():
    response = client.read_all_users()
    users = json.loads(response.text)

    for_multiple_users(users)
