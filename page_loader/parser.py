"""Module for parsing the page and extracting the data."""
import logging
from os import listdir, makedirs, path
from secrets import token_urlsafe
from typing import List
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

# allowed resources for downloading
RESOURCES = {  # noqa: WPS407
    'img': 'src',
    'link': 'href',
    'script': 'src',
}


logger = logging.getLogger(__name__)


def get_resources_links(file_path: str, request_url: str) -> List[tuple]:
    """Get all links of local resources from html file for downloading.

    :param: file_path: path to file for parsing.
    :param: request_url: url of the web page.
    :return: list of tuples with urls for downloading and paths for saving.
    """
    logger.debug(f'get_resources_links file_path: {file_path}, request_url: {request_url}')
    soup = BeautifulSoup(read_file(file_path), 'html.parser')
    links = []
    # get tags with resources
    for tag in soup.find_all(RESOURCES.keys()):
        logger.debug(f'processing tag: {tag}')
        if tag.has_attr(RESOURCES.get(tag.name)):
            # make absolute url from local url

            current_url = tag[RESOURCES[tag.name]]
            resource_url = make_url_absolute(current_url, request_url)
            logger.debug(f'convert url {current_url} to absolute url: {resource_url}')

            # check, if resource is local
            if is_local(resource_url, request_url):
                logger.debug(f'url {resource_url} is local')
                # generate path for saving resource
                local_path = generate_local_path(file_path, resource_url)
                links.append((resource_url, local_path))
                logger.debug(f'add links to list: url for download {resource_url}, path for saving {local_path}')
                # change tag url to local url
                tag[RESOURCES[tag.name]] = local_path

    write_file(file_path, soup)
    logger.debug(f'return {len(links)} links: {str(links)[:200]} ...')  # noqa
    return links


def make_url_absolute(url: str, request_url: str) -> str:
    """Make url absolute.

    :param url: url to make absolute
    :param request_url: request url, contains hostname
    :return: absolute url
    """
    # fix url if it is relative
    if url.startswith('//'):
        url = f'http:{url}'

    if bool(urlparse(url).netloc):
        return url

    return urljoin(request_url, url)


def read_file(file_path: str) -> str:
    """Read file and return content.

    :param file_path: path to file
    :return: content of file
    """
    with open(file_path, encoding='utf-8') as f:
        return f.read()


def write_file(file_path: str, soup: BeautifulSoup):
    """Write file with parsed html (modified links to local resources).

    :param file_path: path to file for saving
    :param soup: modified page source
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify()))


def is_local(resource_url: str, request_url: str) -> bool:
    """Check, is the received path local for host.

    :param resource_url: url of checked resource
    :param request_url: request url, contains hostname
    :return: True if resource is local
    """
    resource_hostname = urlparse(resource_url).hostname
    hostname = urlparse(request_url).hostname
    if (resource_hostname == hostname) or (resource_hostname is None):  # noqa: WPS531
        return True
    return False


def generate_local_path(file_path: str, resource_url: str):
    """Generate path for saving resource.

    :param file_path: path to saved html file
    :param resource_url: parsed url of resource
    :return: path for saving resource
    """
    # generate folder name for resources
    folder_name = f'{path.basename(file_path)[:-5]}_files'
    # generate folder path for resources
    folder_path = path.normpath(path.join(path.dirname(file_path), folder_name))
    # make dir, existed dirs allowed
    makedirs(folder_path, exist_ok=True)
    # get right filename for saving resource: unique and not too long
    resource_name = get_filename(folder_path, resource_url)
    return path.join(folder_path, resource_name)


def get_filename(folder_path: str, resource_url: str, original=False) -> str:
    """Get name for resource from link.

    Cut name for max 30 symbols.
    If name is not unique in folder, add random token to it.

    :param folder_path: path to folder for saving resource
    :param resource_url: url of resource
    :param original: if True, return filename with added extension '_original'

    :return: filename for saving resource
    """
    max_len = 30  # max length of filename
    token_len = 8  # length of random token

    filename = path.basename(urlparse(resource_url).path)  # get filename from url
    name, ext = path.splitext(filename)

    if len(filename) > max_len:  # cut long filenames
        name = f'{name[:max_len]}'

    if f'{name}{ext}' in listdir(folder_path):  # generate unique filename if it exist in folder
        name = f'{name[:max_len]}_{token_urlsafe(token_len)}'

    if original:
        return f'{name}_original{ext}'

    return f'{name}{ext}'
