import sys
import argparse
import logging
from logging.config import dictConfig
from page_loader.logging_config import LOGGING_LEVELS, logger_setup
from page_loader.scripts.definitions import DEFAULT_DIR
from page_loader.loader import download, ExpectedError

SUCCESS_MESSAGE = "Page was successfully downloaded into '{0}'"


def main() -> None:
    """ Main function """
    url, download_dir, logger_level = cli()     # get args from CLI
    logging.config.dictConfig(logger_setup(logger_level))
    logger = logging.getLogger(__name__)

    try:
        saved_page = download(url, download_dir)
    except ExpectedError:
        logging.exception("Web page download failed")
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
                        default='warning',
                        choices=LOGGING_LEVELS.keys(),
                        help='sets log level (default: warning)'
                        )

    args = parser.parse_args()
    return args.url, args.output, args.log_level


if __name__ == '__main__':
    main()

