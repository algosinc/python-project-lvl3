import argparse
import logging
from loader.constants import DEFAULT_DIR


def main():
    download_dir, url, logger_level = cli()
    # ADD setup logging level
    pass


def cli():
    """ CLI interface for app """
    parser = argparse.ArgumentParser(description='Web page downloader')
    parser.add_argument('url', type=str)

    parser.add_argument('-o',
                        '--output',
                        type=str,
                        default=DEFAULT_DIR,
                        help=f'output dir (default: {DEFAULT_DIR})')

    parser.add_argument(
                        '-l',
                        '--log-level',
                        type=str,  # remove if choises
                        default=DEFAULT_LOG_LEVEL,
                        # choices=logging.CONFIGS.keys(),
                        help='sets log level (default: {0})'.format(DEFAULT_LOG_LEVEL),)

    args = parser.parse_args()
    return args.url, args.output, args.log_level


if __name__ == '__main__':
    main()