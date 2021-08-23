import pytest

from framework.api.users_api_client import UsersApiClient


@pytest.mark.smoke
@pytest.mark.user_crud
@pytest.mark.positive
def test_returns_user_list():
    users = UsersApiClient.list_users()
    assert users['per_page'] == len(users['data'])


@pytest.mark.regression
@pytest.mark.user_crud
@pytest.mark.positive
def test_creates_user():
    user_details = {
        'name': 'morpheus',
        'job': 'leader'
    }
    user = UsersApiClient.create_user(user_details)
    assert user['id'] is not None and user['name'] == 'morpheus' and user['job'] == 'leader'


@pytest.mark.regression
@pytest.mark.user_crud
@pytest.mark.positive
def test_returns_user():
    user = UsersApiClient.get_user(user_id=6)
    assert 'data' in user and isinstance(user['data'], dict)


@pytest.mark.regression
@pytest.mark.user_crud
@pytest.mark.negative
def test_fails_get_user():
    user = UsersApiClient.get_user(user_id=66)
    assert 'data' in user and isinstance(user['data'], dict)


@pytest.mark.smoke
@pytest.mark.user_crud
@pytest.mark.positive
def test_updates_user():
    response = UsersApiClient.update_user(user_id=2)
    assert b'updatedAt' in response.content and response.status_code == 200


@pytest.mark.smoke
@pytest.mark.user_crud
@pytest.mark.positive
def test_deletes_user():
    response = UsersApiClient.delete_user(user_id=3)
    assert 'id' not in response and response.status_code == 204


@pytest.mark.slow
@pytest.mark.users_api
@pytest.mark.positive
def test_delayed_response():
    response = UsersApiClient.delayed_response(delay=3)
    assert 'data' in response
