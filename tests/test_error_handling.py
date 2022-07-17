"""Test error handling."""

import os
import pytest
from stat import S_IREAD, S_IRGRP, S_IROTH
from pathlib import Path
from page_loader.loader import download

SAVED_FILE = 'ru-hexlet-io-courses.html'
SAVED_RESOURCE_FILE = 'ru-hexlet-io-courses_files/application.css'


def test_download_wrong_path(tmp_path):
    """Test errors when downloading to non-existing path."""
    # create folder in tmpdir

    test_folder = os.path.realpath(os.path.join(tmp_path, 'test_folder'))
    html_file = os.path.join(test_folder, SAVED_FILE)
    print(f'\nhtml_file {html_file}')
    Path(test_folder).mkdir(parents=True, exist_ok=True)
    with open(html_file, 'x') as f:
        f.write('test')
    # open(html_file, 'x').write('').close()    # noqa WPS515

    os.chmod(html_file, S_IREAD | S_IRGRP | S_IROTH)
    # resource_file = test_folder.join(SAVED_RESOURCE_FILE)
    # os.chmod(resource_file, S_IREAD | S_IRGRP | S_IROTH)
    # html_file.write('test')
    # file.chmod(0o444)


    # wrong_path = os.path.join(tmpdir, '/df#..?^^')
    with pytest.raises(OSError):
        download('https://ru.hexlet.io/courses', test_folder)

    # test_folder = tmp_path / 'test_folder'
    # test_folder.mkdir()
    # # touch file in folder
    # html_file = test_folder / SAVED_FILE
    # html_file.touch()
    # print(f'\nhtml_file {html_file}')
    #open(html_file, 'x').write('').close()    # noqa WPS515