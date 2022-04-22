import logging
import logging.config
import os


def get_logging_structure(LOGFILE_ROOT):

    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': "[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s",
                'datefmt': "%d/%b/%Y %H:%M:%S"
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'data_log_file': {
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOGFILE_ROOT, 'data.log'),
                'formatter': 'verbose'
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            }
        },
        'loggers': {
            'fastapi': {
                'handlers': ['data_log_file'],
                'propagate': True,
                'level': 'DEBUG',
            },
            'critics': {
                'handlers': ['console', 'data_log_file'],
                'level': 'CRITICAL',
            },
        },
        "root": {
            "level": "DEBUG",
            "handlers": ["console", "data_log_file"]
        }
    }


LOGGING = get_logging_structure('_logs')
logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)
