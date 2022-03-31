import logging

LOGGING_CONFIG = {  # noqa: WPS407
    'debug': {
        'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        'level': 'DEBUG',
        'handlers': [
            logging.StreamHandler(),
            logging.FileHandler('page_loader.log'),
        ],
    },
    'warning': {
        'format': '%(asctime)s - %(levelname)s - %(message)s',
        'level': 'WARNING',
        'handlers': [
            logging.StreamHandler(),
            logging.FileHandler('page_loader.log'),
        ],
    },
}


def setup(level):
    logging.basicConfig(
        level=LOGGING_CONFIG[level]['level'],
        format=LOGGING_CONFIG[level]['format'],
        handlers=LOGGING_CONFIG[level]['handlers'],
    )

