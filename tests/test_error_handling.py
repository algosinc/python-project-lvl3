"""Test error handling."""

from os import chmod, makedirs, path
from stat import S_IREAD, S_IRGRP, S_IROTH

import pytest
import requests

from page_loader.loader import download

SAVED_FILE = 'ru-hexlet-io-courses.html'
NETWORK_ERROR_CODE = 404


def test_wrong_path():
    """Test errors handling when downloading to non-existent folder."""
    with pytest.raises(OSError):
        download('https://ru.hexlet.io/courses', '&(#)$%^&*()')


def test_inaccessible(tmp_path):
    """Test errors handling when downloading to write protected folder.

    Create file in test folder and set read only permissions for it.
    :param tmp_path: temporary folder fixture
    """
    html_file = path.join(tmp_path, SAVED_FILE)
    makedirs(path.dirname(html_file), exist_ok=True)
    open(html_file, 'x').close()  # noqa WPS515
    chmod(html_file, S_IREAD | S_IRGRP | S_IROTH)

    with pytest.raises(OSError):
        download('https://ru.hexlet.io/courses', tmp_path)


def test_network_error(tmp_path, requests_mock):
    """Test errors handling when downloading fails.

    :param tmp_path: temporary folder fixture
    :param requests_mock: mock for requests module
    """
    requests_mock.get('https://ru.hexlet.io/courses', status_code=NETWORK_ERROR_CODE)
    with pytest.raises(requests.exceptions.RequestException):
        download('https://ru.hexlet.io/courses', tmp_path)
