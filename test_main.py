import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """Test the hello world endpoint"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Hello, World!' in rv.data
