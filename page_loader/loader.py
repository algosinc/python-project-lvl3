import os
import requests

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


def download(url: str, download_dir=DEFAULT_DIR) -> str:
    """
    Main download function:
        - download and save page in html format
        - parse it for resources
        - save resources to sub folder

    :param url: url for downloading
    :param download_dir: folder name to save
    :return: local path to saved html file for CLI output
    """

    file_path = os.path.join(ROOT_DIR, download_dir, get_filename(url))     # generate absolute path for saving file
    r = requests.get(url)                                                   # download file
    os.makedirs(os.path.dirname(file_path), exist_ok=True)                  # make dir, existed dirs allowed
    with open(file_path, 'w', encoding='utf-8') as f:                       # save file
        f.write(r.text)
    download_resources(file_path, url)
    return os.path.join(download_dir, get_filename(url))         # generate and return relative file path for CLI output


# def download_html()


def download_resources(path: str, url: str) -> None:
    """ Download local resources.
    :param path: path to html file
    :param url: url of the web page
    """
    for file_url, file_path in get_resources_links(path, url):
        response = requests.get(file_url, stream=True)              # download file
        os.makedirs(os.path.dirname(file_path), exist_ok=True)      # make dir, existed dirs allowed
        with open(file_path, 'wb') as f:                            # save file with chunk iteration
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







