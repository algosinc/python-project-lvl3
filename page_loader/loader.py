"""Module for downloading the page and resources."""
import logging
import os
import sys

import requests
from colorama import Fore
from progress.spinner import Spinner

from page_loader.namer import get_page_filename
from page_loader.parser import get_resources_links
from page_loader.scripts.definitions import DEFAULT_DIR, ROOT_DIR

sys.stdout.reconfigure(encoding='utf-8')
logger = logging.getLogger(__name__)


class ExpectedError(Exception):
    """Class for errors expected during execution of program."""

    pass    # noqa


class DownloadSpinner(Spinner):
    """Custom spinner to show progress of local downloads."""

    phases = [Fore.GREEN + '✓ Downloaded: ' + Fore.RESET]


def download(url: str, download_dir=DEFAULT_DIR) -> str:
    """Download web page and local resources to the specified directory.

    :param url: url for downloading
    :param download_dir: folder for saving downloaded files
    :raises OSError: incorrect path
    :raises PermissionError: permission denied

    :return: local path to saved html file for CLI output
    """
    # generate absolute path for saving file
    page_path = os.path.join(ROOT_DIR, download_dir, get_page_filename(url))
    logger.debug(f'Generated path for saving file: {page_path}')

    try:
        os.makedirs(os.path.dirname(page_path), exist_ok=True)      # make dir, existed dirs allowed
    except OSError:
        logger.exception('File system error happened.')
        raise

    try:
        download_path = download_html(url, page_path)
    except PermissionError:
        logger.exception(f'Permission denied for {page_path}')
        raise

    logger.debug(f'Download resources from page: {url}')
    download_resources(download_path, url)

    logger.debug(f'download() return path of saved url: {download_path}')
    return download_path


def download_html(url: str, page_path: str) -> str:
    """Download html file and save it to the specified directory. # noqa DAR003

    :param url: url of the web page
    :param page_path: folder for saving downloaded files
    :raise RequestException: request error
    :return: local path to saved html file for CLI output
    """

    try:
        response = requests.get(url)
        logger.debug(f'Response status code: {response.status_code}')
        response.raise_for_status()
    except requests.exceptions.RequestException:
        logger.exception('Network error happened.')
        raise

    # save page for modification
    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(response.text)
        print(f'⇓ Downloading page: {url}')  # noqa DAR003
        logger.debug(f'Saved page for modification: {page_path}')

    # save original page
    name, ext = os.path.splitext(page_path)
    original_page_path = os.path.join(os.path.dirname(page_path), f'{name}_original{ext}')
    with open(original_page_path, 'w', encoding='utf-8') as f2:
        f2.write(response.text)
        logger.debug(f'Saved original page: {original_page_path}')

    logger.debug(f'Return: {page_path}')
    return page_path


def download_resources(path: str, url: str) -> None:
    """Download local resources.

    :param path: path to html file
    :param url: url of the web page
    """
    logger.debug(f'Download resources from page: {path} / {url}')
    print(f'⇓ Downloading resources from page: {url}')    # noqa DAR003
    spinner = DownloadSpinner()
    for file_url, page_path in get_resources_links(path, url):
        response = requests.get(file_url, stream=True)
        logger.debug(f'download resource {file_url}, response status code: {response.status_code}')
        # download file
        os.makedirs(os.path.dirname(page_path), exist_ok=True)      # make dir, existed dirs allowed
        with open(page_path, 'wb') as f:                            # save file with chunk iteration
            for chunk in response.iter_content(chunk_size=None):
                f.write(chunk)
            logger.debug(f'File saved to {page_path}')
        spinner.next()
        print(file_url)   # noqa DAR003