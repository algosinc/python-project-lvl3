import argparse
from page_loader.scripts.config.definitions import DEFAULT_DIR, DEFAULT_LOG_LEVEL
from page_loader.loader import download


def main():
    url, download_dir, logger_level = cli()
    # ADD setup logging level
    saved_page = download(url, download_dir)
    print(saved_page)


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