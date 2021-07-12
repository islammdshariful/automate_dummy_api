import random
from json import dumps
from uuid import uuid4

from clients.users.base_client import BaseClient
from config import BASE_URL
from utils.request import APIRequest


def get_user_url(user_id):
    url = f'{BASE_URL}users/{user_id}'
    return url


class UserClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.base_url = BASE_URL
        self.request = APIRequest()

    def create_user(self, body=None):
        username, response = self.__create_user_with_unique_username(body)
        return username, response

    def __create_user_with_unique_username(self, body=None):
        if body is None:
            username = f'mr{str(uuid4())}'
            payload = dumps({
                "name": "Mr. Number" + str(random. randint(0, 999)),
                "username": username,
                "email": username + "@faki.api",
                "address": {
                    "street": "Kulas Light",
                    "suite": "Apt. 556",
                    "city": "Gwenborough",
                    "zipcode": "92998-3874",
                    "geo": {
                        "lat": "-37.3159",
                        "lng": "81.1496"
                    }
                },
                "phone": str(random. randint(0, 99999999999)),
                "website": "fakiapi.user." + username + ".fk",
                "company": {
                    "name": "FakiAPI",
                    "catchPhrase": "Lorem Ipsum is simply a dummy text.",
                    "bs": "lorem-ipsum-is-simply-a-dummy-text"
                }
            })
        else:
            username = body['username']
            payload = dumps(body)

        response = self.request.post(self.base_url, payload, self.headers)
        return username, response

    def read_one_user_by_id(self, person_id):
        people = get_user_url(person_id)
        return self.request.get(people)

    def read_all_users(self):
        return self.request.get(self.base_url)

    def update_user(self, person_id, payload):
        people = get_user_url(person_id)
        return self.request.put(people, payload, self.headers)

    def delete_user(self, person_id):
        url = f'{BASE_URL}users/{person_id}'
        return self.request.delete(url)
