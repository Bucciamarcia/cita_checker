import logging
import sys


def get_logger(name):
    logger = logging.getLogger(name)
    if sys.gettrace():
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.WARNING)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
