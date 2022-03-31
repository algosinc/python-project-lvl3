import os
import requests
import logging

from page_loader.namer import get_filename
#from page_loader.parser import get_resources_links
from page_loader.scripts.definitions import ROOT_DIR, DEFAULT_DIR


'''
Задачи
Добавьте в тесты проверку скачивания изображений и изменения HTML.
Измените HTML так, чтобы все ссылки указывали на скачанные файлы.
Добавьте в ридми аскинему с примером работы пакета.
Подсказки
Beautiful Soup может ломать отступы и кодировку после изменения HTML-файла, учитывайте это в фикстурах.
При изменении HTML с помощью Beautiful Soup используйте значение по умолчанию форматера prettify().
Для парсинга html используйте html.parser.
'''

logger = logging.getLogger(__name__)

class ExpectedError(Exception):
    """Class for errors expected during excecution of programm."""

    pass


def download(url: str, download_dir=DEFAULT_DIR) -> str:
    """ Download web page and local resources to the specified directory.

    :param url: url for downloading
    :param download_dir: folder for saving downloaded files
    :return: local path to saved html file for CLI output
    :raises ExpectedError: permission denied or incorrect path
    """

    page_path = os.path.join(ROOT_DIR, download_dir, get_filename(url))     # generate absolute path for saving file

    try:
        os.makedirs(os.path.dirname(page_path), exist_ok=True)      # make dir, existed dirs allowed
    except FileNotFoundError:
        raise ExpectedError(
            f'Make sure that you have chosen the correct directory for saving files. {page_path}')
    except PermissionError:
        raise ExpectedError(
            f'Make sure that you have permissions to write in the chosen directory. {page_path}')
    except OSError as err:
        raise ExpectedError(
            f'Unknown error happened. {err}')

    download_path = download_html(url, page_path)
    # download_resources(page_path, url)
    # os.path.join(download_dir, get_filename(url))         # generate and return relative file path for CLI output
    return download_path


def download_html(url: str, page_path: str) -> str:
    """
    Download html file and save it to the specified directory
    :param url: url of the web page
    :param page_path: folder for saving downloaded files
    :return: local path to saved html file for CLI output
    :raises ExpectedError: network error
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        raise ExpectedError(
            f'Network error {err} when downloading {url}. Status code: {requests.get(url).status_code}')

    with open(page_path, 'w', encoding='utf-8') as f:  # save file
        f.write(response.text)
    return page_path


def download_resources(path: str, url: str) -> None:
    """ Download local resources.
    :param path: path to html file
    :param url: url of the web page
    """
    for file_url, page_path in get_resources_links(path, url):
        response = requests.get(file_url, stream=True)              # download file
        os.makedirs(os.path.dirname(page_path), exist_ok=True)      # make dir, existed dirs allowed
        with open(page_path, 'wb') as f:                            # save file with chunk iteration
            for chunk in response.iter_content(chunk_size=None):
                f.write(chunk)




def make_dir_for_resources(filename):
    """
    Make a dir like filename_files
    """
    pass



def is_unic_name(filename, path):
    """
    check is file has unique filename in resources folder
    if not - generate new and unique
    :param filename:
    :param path: path to resource folder
    :return: unique filename
    """







