import pytest
from django.urls import reverse
from django.test import Client


@pytest.fixture
def api_client():
    return Client()


@pytest.mark.parametrize(
    'data, response_content',
    [
        (
            {},
            {'content': 'OK', 'errorList': []},
        ),
        (
            {'test': 123},
            {'content': '', 'errorList': ['ERROR']},
        ),
    ],
)
def test_endpoint(api_client, data, response_content):
    response = api_client.post('', data)
    assert response.status_code == 200
    assert response.json() == response_content

