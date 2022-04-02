
LOGGING_LEVELS = {
    'debug': 'DEBUG',
    'info': 'INFO',
    'warning': 'WARNING',
    'error': 'ERROR',
    'critical': 'CRITICAL',
}


def logger_setup(level):
    log_level = LOGGING_LEVELS.get(level)

    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,

        'formatters': {
            'default_formatter': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
        },

        'handlers': {
            'stream_handler': {
                'class': 'logging.StreamHandler',
                'formatter': 'default_formatter',
            },
            'file_handler': {
                'class': 'logging.FileHandler',
                'formatter': 'default_formatter',
                'filename': 'page_loader.log',
                'encoding': 'utf-8',
            },
        },

        'loggers': {
            'page_loader': {
                'handlers': ['stream_handler', 'file_handler'],
                'level': log_level,
            }
        }
    }

    return logging_config
