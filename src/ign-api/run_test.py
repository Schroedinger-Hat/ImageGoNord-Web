import base64
import io

import pytest
from PIL import Image

from run import app, API_VERSION
from flask.testing import FlaskClient
from img_test import img


@pytest.fixture
def client():
    """Creating client"""
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


@pytest.fixture
def base64_pixel():
    return img


def get_img_size(base64_str: str):
    imgdata = base64.b64decode(base64_str)
    im = Image.open(io.BytesIO(imgdata))
    return im.size  # width, height


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


def test_quantize_api(client: FlaskClient, base64_pixel):
    URL = API_VERSION + '/quantize'
    data = {'b64_input': base64_pixel, 'b64_output': True}
    response = client.post(URL, data=data, content_type='multipart/form-data')
    assert response.status_code == 200

    json = response.json
    assert 'success' in json.keys()
    assert json['success']
    assert 'b64_img' in json.keys()


def test_quantize_api_no_data_provided(client: FlaskClient):
    URL = API_VERSION + '/quantize'
    data = {'b64_output': True}
    response = client.post(URL, data=data, content_type='multipart/form-data')
    assert response.status_code == 400


def test_image_resize_convert(client: FlaskClient, base64_pixel):
    URL = API_VERSION + '/convert'
    data = {'width': 100, 'height': 100, 'b64_input': base64_pixel, 'b64_output': True}
    response = client.post(URL, data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert get_img_size(response.json.get('b64_img')) == (100, 100)


def test_image_resize_quantize(client: FlaskClient, base64_pixel):
    URL = API_VERSION + '/quantize'
    data = {'width': 100, 'height': 100, 'b64_input': base64_pixel, 'b64_output': True}
    response = client.post(URL, data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert get_img_size(response.json.get('b64_img')) == (100, 100)
