import logging
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
            'profiles_file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOGFILE_ROOT, 'profiles.log'),
                'formatter': 'verbose'
            },
            'data_log_file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOGFILE_ROOT, 'data.log'),
                'formatter': 'verbose'
            },
            'fastapi_log_file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOGFILE_ROOT, 'fastapi.log'),
                'formatter': 'verbose'
            },
            'proj_log_file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOGFILE_ROOT, 'project.log'),
                'formatter': 'verbose'
            },
            'route_updater': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOGFILE_ROOT, 'route.updater.log'),
                'formatter': 'verbose'
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            }
        },
        'loggers': {
            'profiles': {
                'handlers': ['console', 'profiles_file'],
                'level': 'DEBUG',
            },

            'fastapi': {
                'handlers': ['fastapi_log_file'],
                'propagate': True,
                'level': 'ERROR',
            },
            'project': {
                'handlers': ['proj_log_file'],
                'level': 'DEBUG',
            },
            'route_updater': {
                'handlers': ['console', 'route_updater'],
                'level': 'DEBUG',
            },
        }
    }
    
    
LOGGING = get_logging_structure('_logs')
