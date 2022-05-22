"""Create a temporary directory for testing."""
import pytest


@pytest.fixture(scope='session')
def tmpdir_download(tempdir_factory):
    """Create a temporary directory for downloads.

    :param tempdir_factory: fixture for create temporary directory
    :return: temporary directory
    """


    return tempdir_factory.mktemp('tmp_downloads')