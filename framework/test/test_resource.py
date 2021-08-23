import pytest
from requests.exceptions import HTTPError

from framework.api.resource_api_client import ResourceApiClient


@pytest.mark.smoke
@pytest.mark.resource_crud
@pytest.mark.positive
def test_returns_resources_list():
    resources_list = ResourceApiClient.list_resource()
    assert resources_list['total_pages'] >= resources_list['page']


@pytest.mark.smoke
@pytest.mark.resource_crud
@pytest.mark.positive
def test_returns_resource():
    list_of_unknown = ResourceApiClient.get_resource(resource_id=2)
    assert list_of_unknown['total_pages'] >= list_of_unknown['page']


@pytest.mark.smoke
@pytest.mark.user_crud
@pytest.mark.should_raise
def test_fails_get_resource():
    with pytest.raises(HTTPError):
        resource = ResourceApiClient.get_resource(resource_id=23)
        assert 'data' not in resource
