import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_serve_index(client):
    """Test that the index.html file is served"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'<title>My Awesome App</title>' in rv.data
