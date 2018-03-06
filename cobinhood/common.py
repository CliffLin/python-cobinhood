"""
Common Library
"""
import logging
import coloredlogs
from cobinhood.configuration import Config

LOG = logging.getLogger('cobinhood')


def Authorization(func):
    """
    Check API TOKEN is Existed
    """
    def _wrapped(*args):
        if not Config.API_TOKEN:
            LOG.error('NO API TOKEN')
            return None
        return func(*args)
    return _wrapped


def logger(level='DEBUG', obj='cobinhood'):
    """
    logger function
    """
    def decorator(func):
        def _wrapped(*args):
            coloredlogs.install(level=Config.LOG_LEVEL, logger=LOG)

            if level == 'DEBUG':
                LOG.debug('%s fetch "%s"', obj, func.__name__)
            elif level == 'INFO':
                LOG.info('%s fetch "%s"', obj, func.__name__)
            return func(*args)
        return _wrapped
    return decorator
