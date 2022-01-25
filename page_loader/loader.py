import os
import re
from urllib.parse import urlparse
from page_loader.scripts.config.definitions import ROOT_DIR, DEFAULT_DIR

import requests

"""
Реализуйте утилиту командной строки page-page_loader, которая, скачивает страницу из сети и кладет в указанную существующую 
директорию (по умолчанию в директорию запуска программы). Программа должна выводить на экран полный путь к загруженному файлу.

На данном этапе не производятся манипуляции с содержимым, только сохранение.

# по умолчанию output это os.getcwd()
$ page-page_loader --output /var/tmp https://ru.hexlet.io/courses
/var/tmp/ru-hexlet-io-courses.html  # путь к загруженному файлу

from page_loader import download

file_path = download('https://ru.hexlet.io/courses', '/var/tmp')
print(file_path)  # => '/var/tmp/ru-hexlet-io-courses.html'
То есть ваша библиотека должна предоставлять модуль page_loader с функцией download(), вызов которой скачивает страницу 
из сети в указанную существующую директорию и возвращает полный путь к загруженному файлу, включая имя самого файла.

Имя файла должно формироваться следующим образом:

Берется адрес страницы без схемы
Все символы, кроме букв и цифр, заменяются на дефис -.
В конце ставится .html.
Пример:

https://ru.hexlet.io/courses
ru-hexlet-io-courses.html
"""


def download(url, download_dir=DEFAULT_DIR):
#    filename = os.path.basename(urlparse(url).path)

    path = os.path.join(ROOT_DIR, download_dir, get_filename(url))
    local_path = os.path.join(download_dir, get_filename(url))
    r = requests.get(url)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    with open(local_path, 'w', encoding='utf-8') as f:
        f.write(r.text)
    return local_path


def get_filename(url, ext='.html'):
    u = urlparse(url)
    parsed_url = u.hostname + u.path
    url_head, url_tail = os.path.splitext(parsed_url)

    if url_tail == ext:
        return f'{filename_convert(url_head)}{ext}'

    return f'{filename_convert(parsed_url)}{ext}'


def filename_convert(filename):
    return re.sub(f'\W', '-', filename)


def main():
    print(get_filename('https://www.geeksforgeeks.org/python-os-path-join-method'))
    print(get_filename('https://www.geeksforgeeks.org/python-os-path-join-method/blabka.html'))
    print(download('https://www.nepremicnine.net/novogradnje.html'))

if __name__ == '__main__':
    main()





