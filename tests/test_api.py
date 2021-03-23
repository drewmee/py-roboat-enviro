import json

import pytest


class TestUsers:
    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        self.api_client = api_client

    def test_get_users(self):
        response = self.api_client.get_users("drewm")
        assert response.ok
        assert response.json()
        print(response.json())

    def test_search(self):
        filters = [{"field": "id", "op": "<", "value": 24}]
        filters = json.dumps(filters)
        response = self.api_client.search_users(filters)
        assert response.ok
