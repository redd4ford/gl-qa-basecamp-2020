import requests
from urllib.parse import urljoin

from framework.config.config import Config
from framework.config.endpoints import Endpoints


class ResourceApiClient:
    URL = ''

    @staticmethod
    def _prepare_url(base_url=Config.BASE_URL, url=''):
        return urljoin(base_url, url)

    @staticmethod
    def list_resource():
        response = requests.get(
            ResourceApiClient._prepare_url(url=Endpoints.RESOURCE_URL)
        )
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_resource(resource_id: int):
        response = requests.get(
            ResourceApiClient._prepare_url(url=f'{Endpoints.RESOURCE_URL}/{resource_id}')
        )
        response.raise_for_status()
        return response.json()
