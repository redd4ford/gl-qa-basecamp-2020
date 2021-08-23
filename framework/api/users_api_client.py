import requests
from urllib.parse import urljoin

from framework.config.config import Config
from framework.config.endpoints import Endpoints


class UsersApiClient:
    URL = ''

    @staticmethod
    def _prepare_url(base_url=Config.BASE_URL, url=''):
        return urljoin(base_url, url)

    @staticmethod
    def list_users():
        response = requests.get(
            url=UsersApiClient._prepare_url(url=Endpoints.USERS_URL)
        )
        response.raise_for_status()
        return response.json()

    @staticmethod
    def create_user(user_details: dict):
        response = requests.post(
            url=UsersApiClient._prepare_url(url=Endpoints.USERS_URL),
            json=user_details
        )
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_user(user_id: int):
        return requests.get(
            url=UsersApiClient. _prepare_url(url=f'{Endpoints.USERS_URL}/{user_id}'),
        ).json()

    @staticmethod
    def update_user(user_id: int):
        return requests.put(
            url=UsersApiClient. _prepare_url(url=f'{Endpoints.USERS_URL}/{user_id}'),
        )

    @staticmethod
    def delete_user(user_id: int):
        return requests.delete(
            url=UsersApiClient. _prepare_url(url=f'{Endpoints.USERS_URL}/{user_id}'),
        )

    @staticmethod
    def register(user_details: dict):
        response = requests.post(
            UsersApiClient._prepare_url(url=Endpoints.REGISTER_URL),
            json=user_details
        )
        response.raise_for_status()
        return response.json()

    @staticmethod
    def login(user_details: dict):
        response = requests.post(
            UsersApiClient._prepare_url(url=Endpoints.LOGIN_URL),
            json=user_details
        )
        response.raise_for_status()
        return response.json()

    @staticmethod
    def delayed_response(delay: int):
        response = requests.get(
            UsersApiClient._prepare_url(url=f'{Endpoints.USERS_URL}?delay={delay}')
        )
        response.raise_for_status()
        return response.json()
