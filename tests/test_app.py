"""Integration tests for app.py"""
import pytest

from bank_api.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_account_creation(client):
    # Use the client to make request client.post(...)
    response_post =client.post('/accounts/test')
    assert response_post.status_code == 200

def test_account_retrieve(client):   
    # Use the client to make request client.get(...)
    response_get = client.get('/accounts/test')
    assert response_get.status_code == 200