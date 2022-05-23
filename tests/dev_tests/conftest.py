"""Create a temporary directory for testing."""
import pytest


@pytest.fixture(scope='session')
def download_tmpdir(tmpdir_factory):
    """Create a temporary directory for downloads.

    :param tmpdir_factory: fixture for create temporary directory
    :return: temporary directory
    """
    return tmpdir_factory.mktemp('tmp_downloads')