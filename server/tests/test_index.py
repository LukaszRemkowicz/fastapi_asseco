import json
from unittest import TestCase

from fastapi.testclient import TestClient

from server.app.index import app


class TestIndex(TestCase):

    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_endpoint_response(self) -> None:
        """ check if response status is 200 """

        url = '/'
        response = self.client.get(url)

        assert response.status_code == 200

    def test_response_obj(self):
        """ check if response is dict and includes date and ip """

        url = '/'
        response = self.client.get(url)
        response = json.loads(response.content.decode('utf-8'))

        assert isinstance(response, dict)
        assert response.get('date')
        assert any([key for key in response.keys() if 'ip' in key])

    def test_if_no_post_method(self):
        """ Test if endpoint not allows post method """

        url = '/'
        response = self.client.post(url)

        assert response.status_code == 405
