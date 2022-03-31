import sys
import argparse
import logging
from page_loader import logging_config
from page_loader.scripts.definitions import DEFAULT_DIR, DEFAULT_LOG_LEVEL
from page_loader.loader import download, ExpectedError

SUCCESS_MESSAGE = "Page was successfully downloaded into '{0}'"
logger = logging.getLogger(__name__)


def main() -> None:
    """ Main function """
    url, download_dir, logger_level = cli()  # get args from CLI
    try:
        saved_page = download(url, download_dir)
    except ExpectedError as err:
        logger.error(err)
        sys.exit(1)
    print(SUCCESS_MESSAGE.format(saved_page))
    sys.exit(0)


def cli() -> (str, str, str):
    """ CLI interface for the app """

    parser = argparse.ArgumentParser(description='Web page downloader')
    parser.add_argument('url',
                        help='url to download',
                        type=str
                        )

    parser.add_argument('-o',
                        '--output',
                        type=str,
                        default=DEFAULT_DIR,
                        help=f'output dir (default: {DEFAULT_DIR})'
                        )

    parser.add_argument(
                        '-l',
                        '--log-level',
                        type=str,
                        default=DEFAULT_LOG_LEVEL,
                        choices=logging_config.LOGGING_CONFIG.keys(),
                        help='sets log level (default: {0})'.format(DEFAULT_LOG_LEVEL)
                        )

    args = parser.parse_args()
    return args.url, args.output, args.log_level


if __name__ == '__main__':
    main()