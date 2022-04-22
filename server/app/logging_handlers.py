import sys
from app.logging_setup import logger


def handle_exception(exc_type, exc_value, exc_traceback):
    """ example how to handle critical logging """

    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logger.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception
