"""This is entry point for the page_loader package."""
import argparse
import logging
import sys
from logging.config import dictConfig

from colorama import Fore

from page_loader.loader import ExpectedError, download
from page_loader.logging_config import LOGGING_LEVELS, logger_setup
from page_loader.scripts.definitions import DEFAULT_DIR

SUCCESS_MESSAGE = f"{Fore.GREEN}Page was successfully downloaded into '{0}'{Fore.RESET}"


def main() -> None:
    """Get url, output dir and log level from CLI."""
    url, download_dir, logger_level = cli()  # get args from CLI
    dictConfig(logger_setup(logger_level))
    logger = logging.getLogger(__name__)

    try:
        saved_page = download(url, download_dir)
    except ExpectedError:
        logger.exception('Web page download failed')
        sys.exit(1)

    sys.stdout.write(f"{Fore.GREEN}✓ Page was successfully downloaded into: '{saved_page}'{Fore.RESET}")  # noqa: WPS221
    sys.exit(0)


def cli() -> (str, str, str):
    """CLI interface for the app."""
    parser = argparse.ArgumentParser(description='Web page downloader')
    parser.add_argument(
        'url',
        help='url to download',
        type=str,
    )

    parser.add_argument(
        '-o',
        '--output',
        type=str,
        default=DEFAULT_DIR,
        help=f'output dir (default: {DEFAULT_DIR})',
    )

    parser.add_argument(
        '-l',
        '--log-level',
        type=str,
        default='warning',
        choices=LOGGING_LEVELS.keys(),
        help='sets log level (default: warning)',
    )

    args = parser.parse_args()
    return args.url, args.output, args.log_level


if __name__ == '__main__':
    main()
