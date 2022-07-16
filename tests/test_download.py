"""Test download functionality."""
import os

from page_loader.loader import download

REMOTE_PAGE = ('tests/fixtures/remote_page.html',)
SAVED_PAGE = ('tests/fixtures/saved_page.html',)

LOCALS_FIXTURES = (
    'tests/fixtures/resource_files/python.png',
    'tests/fixtures/resource_files/runtime.js',
    'tests/fixtures/resource_files/application.css',
)

MOCKING_FIXTURES = REMOTE_PAGE + LOCALS_FIXTURES
SAVED_FIXTURES = SAVED_PAGE + LOCALS_FIXTURES

TEST_URL = 'https://ru.hexlet.io/courses'

MOCKING_LINKS = (
    TEST_URL,
    'https://ru.hexlet.io/assets/professions/python.png',
    'https://ru.hexlet.io/packs/js/runtime.js',
    'https://ru.hexlet.io/assets/application.css',
)


def get_download_paths(download_path):
    """Generate paths to the downloaded files."""
    return (
        os.path.join(
            download_path, 'ru-hexlet-io-courses.html',
        ),
        os.path.join(
            download_path, 'ru-hexlet-io-courses_files/python.png',
        ),
        os.path.join(
            download_path, 'ru-hexlet-io-courses_files/runtime.js',
        ),
        os.path.join(
            download_path, 'ru-hexlet-io-courses_files/application.css',
        ),
    )


def mock_requests(requests_mock):
    """Mock response for requests.get."""
    # prepare mock response from fixtures
    for fixture, link in zip(MOCKING_FIXTURES, MOCKING_LINKS):
        with open(fixture, 'rb') as fixture_file:
            mocking_content = fixture_file.read()
        requests_mock.get(link, content=mocking_content)


def test_download_files(tmpdir, requests_mock):
    """Test download functionality."""
    mock_requests(requests_mock)
    # download the page and get the path to the downloaded file
    download_path = os.path.dirname(download(TEST_URL, tmpdir))

    # check that the downloaded files are equal to the fixtures
    for fixture, local in zip(SAVED_FIXTURES, get_download_paths(download_path)):  # noqa: WPS440
        with open(fixture, 'rb') as fixture_file:  # noqa: WPS440
            with open(local, 'rb') as downloaded_file:
                assert fixture_file.read() == downloaded_file.read()
