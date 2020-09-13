import pytest

from run import app, API_VERSION
from flask.testing import FlaskClient


@pytest.fixture
def client():
    """Creating client"""
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


@pytest.fixture
def base64_pixel():
    """ Base64 JPG pixel 1x1 Blue"""
    return '/9j/4AAQSkZJRgABAQAAAQABAAD//gAfQ29tcHJlc3NlZCBieSBqcGVnLXJlY29tcHJlc3P/2wC' \
           'EAAQEBAQEBAQEBAQGBgUGBggHBwcHCAwJCQkJCQwTDA4MDA4MExEUEA8QFBEeFxUVFx4iHRsdIiol' \
           'JSo0MjRERFwBBAQEBAQEBAQEBAYGBQYGCAcHBwcIDAkJCQkJDBMMDgwMDgwTERQQDxAUER4XFRUXHiId' \
           'Gx0iKiUlKjQyNEREXP/CABEIAAEAAQMBIgACEQEDEQH/xAAUAAEAAAAAAAAAAAAAAAAAAAAI/9oACAEBAAA' \
           'AABz/AP/EABQBAQAAAAAAAAAAAAAAAAAAAAj/2gAIAQIQAAAAf3//xAAUAQEAAAAAAAAAAAAAAAAAAAAG' \
           '/9oACAEDEAAAACv/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/9oACAEBAAE/AH//xAAUEQEAAAAAAAAAAAAAAAAA' \
           'AAAA/9oACAECAQE/AH//xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oACAEDAQE/AH//2Q=='


def test_status_api(client: FlaskClient):
    URL = API_VERSION + '/status'
    response = client.get(URL)
    assert response.status_code == 200
    assert response.json == {'ok': True}


def test_convert_api(client: FlaskClient, base64_pixel):
    URL = API_VERSION + '/convert'
    data = {'b64_input': base64_pixel, 'b64_output': True}
    response = client.post(URL, data=data, content_type='multipart/form-data')
    assert response.status_code == 200

    json = response.json
    assert 'success' in json.keys()
    assert json['success']
    assert 'b64_img' in json.keys()


def test_convert_api_no_data_provided(client: FlaskClient):
    URL = API_VERSION + '/convert'
    data = {'b64_output': True}
    response = client.post(URL, data=data, content_type='multipart/form-data')
    assert response.status_code == 400
