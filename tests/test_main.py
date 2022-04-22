"""Test common app functionality."""

import os
import sys

import pytest

from page_loader.scripts.main import main

DIR_TO_SAVE = 'tests/tmp_downloads'
TEST_URL = 'https://habr.ru'
SAVED_FILE = r'page_loader\scripts\tmp2\habr-ru.html'
EXPECTED_OUTPUT = ''

# Howto test
# - create fixture that create tmpdir
# - send args and check CLI output
# - check if file was created and content is correct
# - check if right resources were downloaded: check names and hashes
# - remove tmpdir after test


@pytest.mark.parametrize(
    'dir_to_save',
    'test_url',
    'saved_file_path',
    'expected_output',
    [DIR_TO_SAVE, TEST_URL, SAVED_FILE, EXPECTED_OUTPUT],
)
def test_main(monkeypatch):
    """Test main."""
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', ['page-loader', '-o', 'tmp2', TEST_URL])
        assert os.path.exists(SAVED_FILE)
