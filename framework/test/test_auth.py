import pytest
from requests.exceptions import HTTPError

from framework.api.users_api_client import UsersApiClient


@pytest.mark.regression
@pytest.mark.user_auth
@pytest.mark.positive
def test_can_register():
    user_details = {
        'email': 'eve.holt@reqres.in',
        'password': 'pistol'
    }
    reg_details = UsersApiClient.register(user_details)
    assert reg_details['id'] is not None and reg_details['token'] is not None


@pytest.mark.smoke
@pytest.mark.user_auth
@pytest.mark.should_raise
def test_fails_on_register():
    user_details = {
        'password': 'pistol'
    }
    with pytest.raises(HTTPError):
        UsersApiClient.register(user_details)

    user_details = {
        'email': 'eve.holt@reqres.in'
    }
    with pytest.raises(HTTPError):
        UsersApiClient.register(user_details)


@pytest.mark.regression
@pytest.mark.user_auth
@pytest.mark.positive
def test_can_login():
    user_credentials = {
        'email': 'eve.holt@reqres.in',
        'password': 'pistol'
    }
    login_info = UsersApiClient.login(user_credentials)
    assert login_info['token'] is not None


@pytest.mark.smoke
@pytest.mark.user_auth
@pytest.mark.should_raise
def test_fails_on_login():
    user_credentials = {
        'email': 'eve.holt@reqres.in',
    }
    with pytest.raises(HTTPError):
        UsersApiClient.login(user_credentials)

    user_credentials = {
        'password': 'pistol'
    }
    with pytest.raises(HTTPError):
        UsersApiClient.login(user_credentials)
