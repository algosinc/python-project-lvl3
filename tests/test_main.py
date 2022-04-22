"""Test common app functionality."""

import os
import sys

import pytest

from page_loader.scripts.main import main

DIR_TO_SAVE = 'tests/tmp_downloads'
TEST_URL = 'https://habr.ru'
SAVED_FILE = r'page_loader\scripts\tmp2\habr-ru.html'
EXPECTED_OUTPUT = 'tests/fixtures/expected_cli_output.txt'

# Howto test
# - create fixture that create tmpdir
# - send args and check CLI output
# - check if file was created and content is correct
# - check if right resources were downloaded: check names and hashes
# - remove tmpdir after test


@pytest.mark.parametrize(
    'dir_to_save, test_url, saved_file, expected_output',
    [DIR_TO_SAVE, TEST_URL, SAVED_FILE, EXPECTED_OUTPUT],
)
def test_main_cli(capsys, monkeypatch, dir_to_save, test_url, saved_file, expected_output):
    """Test main. Send args and check CLI output. Check if file was created and content is correct."""
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', ['page-loader', '-o', dir_to_save, test_url])
        assert os.path.exists(saved_file)

        captured = capsys.readouterr()
        with open(expected_output, 'r') as expected_cli_output:
            assert captured.out == expected_cli_output.read()
        assert captured.out == expected_output

