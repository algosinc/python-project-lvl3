"""Test common app functionality."""

import os
import sys

import pytest

from page_loader.scripts.main import main

TEST_URL = 'https://habr.ru'
SAVED_FILE = r'page_loader\scripts\tmp2\habr-ru.html'

# HoWto test
# - send args
# - check if file was created
# - check if resources were downloaded
# - check if

@pytest.mark.parametrize('test_url', 'saved_file_path'(
    ['-o', '/tmp/', 'https://example.com'],
def test_main(monkeypatch):
    """Test main."""
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', ['page-loader', '-o', 'tmp2', TEST_URL])
        assert os.path.exists(SAVED_FILE)


