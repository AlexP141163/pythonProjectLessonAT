import pytest
from main_3 import get_random_cat_image
from requests.exceptions import RequestException

def test_successful_request(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"url": "https://cdn2.thecatapi.com/images/12345.jpg"}]
    mocker.patch('requests.get', return_value=mock_response)

    result = get_random_cat_image()
    assert result == "https://cdn2.thecatapi.com/images/12345.jpg"

def test_unsuccessful_request(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mock_response.json.return_value = []
    mocker.patch('requests.get', return_value=mock_response)

    result = get_random_cat_image()
    assert result is None

def test_request_exception(mocker):
    mocker.patch('requests.get', side_effect=RequestException)

    result = get_random_cat_image()
    assert result is None
