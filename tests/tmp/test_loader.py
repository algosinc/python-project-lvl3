'''
Тестируем:
- работа с командной строкой
- нужный файл создается в папке при запросе с урла
- http запрос мокается
- для загрузки создается временная директория
- тестируем случай, когда урл недоступен
'''
import os, pytest
from tempfile import TemporaryDirectory
from page_loader import download
from page_loader.scripts.main import cli

TEST_URL = 'https://ru.hexlet.io/pages/about'


def read_file(path):
    with open(path, encoding="utf8") as f:
        return f.read()


# @pytest.mark.parametrize('args', (
#     ['-o', '/tmp/', 'https://example.com'],
#     ['--output', '/tmp/', 'https://example.com'],
    # ['-o', '/tmp/', '-l', 'INFO', 'https://example.com'],
    # ['-o', '/tmp/', '-l', 'DEBUG', 'https://example.com'],
# ))
# def test_parse_args(args):
#     cli().parse_args(args)


def test_download(requests_mock):
    expected_data = read_file('./tests/fixtures/ru-hexlet-io-pages-about.html')
    requests_mock.get(TEST_URL, text=expected_data)
    with TemporaryDirectory() as tmpdir:
        download(TEST_URL, tmpdir)
        actual = read_file(os.path.join(tmpdir, 'ru-hexlet-io-pages-about.html'))
        assert actual == expected_data

# def test_simple(requests_mock):
#     requests_mock.get('http://test.com', text='data')
#     assert 'data' == requests.get('http://test.com').text
