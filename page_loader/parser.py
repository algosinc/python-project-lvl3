import os
from secrets import token_urlsafe
from bs4 import BeautifulSoup
from typing import List
from urllib.parse import urlparse, urljoin
from page_loader.scripts.definitions import ALLOWED_TAGS
'''
+ get file_path, resources_path
+ open html file and read
+ parse it for resources
- check, if resource is local
- change links from web to local storage
- add to queue list for downloading
- return queue
'''


RESOURCES = {  # noqa: WPS407
    'img': 'src',
    'link': 'href',
    'script': 'src',
}


def get_resources_links(file_path: str, request_url: str) -> List[tuple]:
    '''

    :param file_path: path to file for parsing
    :param request_url: url of the web page
    :return: list of tuples with urls for downloading and paths for saving
    '''

    soup = BeautifulSoup(read_file(file_path), 'html.parser')
    links = []
    for tag in soup.find_all(RESOURCES.keys()): # получили теги
        try:
            resource_url = tag[RESOURCES[tag.name]]
        except KeyError:
            continue
        # check, that link is local
        if not is_local(resource_url, request_url):
            continue
        # generate path for saving resource
        local_path = generate_local_path(file_path, resource_url)
        links.append((make_url_absolute(resource_url, request_url), local_path))
        tag[RESOURCES[tag.name]] = local_path

    print(soup)
    write_file(file_path, soup)
    print(links)
    return links


def make_url_absolute(url, request_url):
    if bool(urlparse(url).netloc):
        return url
    else:
        return urljoin(request_url, url)


def read_file(path):
    with open(path, encoding="utf8") as f:
        return f.read()


def write_file(path, soup):
    with open(path, 'w', encoding="utf8") as f:
        f.write(soup.prettify())


def is_local(resource_url: str, request_url: str) -> bool:
    """ Check, is the received path local for host

    :param resource_url: url of checked resource
    :param request_url: request url, contains hostname
    :return: True if resource is local
    """
    resource_hostname = urlparse(resource_url).hostname
    hostname = urlparse(request_url).hostname
    if (resource_hostname == hostname) or (resource_hostname is None):
        return True
    else:
        return False


def generate_local_path(file_path: str, resource_url: str):
    """ Generate path for saving resource

    :param file_path: path to saved html file
    :param resource_url: parsed url of resource
    :return: path for saving resource
    """
    # generate folder name for resources
    folder_name = os.path.basename(file_path)[0:-5] + '_files'
    # generate folder path for resources
    folder_path = os.path.normpath(os.path.join(os.path.dirname(file_path), folder_name))
    # make dir, existed dirs allowed
    os.makedirs(folder_path, exist_ok=True)
    # get right filename for saving resource: unique and not too long
    resource_name = get_resource_name(folder_path, resource_url)
    return os.path.join(folder_path, resource_name)


def get_resource_name(folder_path: str, resource_url: str) -> str:
    """
    Get name for resource from link:
    - cut name max 20 symbols
    - if filename is not unique for folder, add random token
    :param folder_path:
    :param resource_url:
    :return:
    """
    filename = os.path.basename(urlparse(resource_url).path)    # get filename from url
    name, ext = os.path.splitext(filename)
    if len(filename) > 30:                                      # cut long filenames
        filename = f'{name[:30]}{ext}'

    if filename in os.listdir(folder_path):                     # generate unique filename if it exist in folder
        return f'{name[:30]}_{token_urlsafe(8)}{ext}'

    return filename




