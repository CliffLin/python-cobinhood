"""
Common Library
"""
import logging
import coloredlogs

LOG = logging.getLogger('cobinhood-api')


def logger(level='DEBUG', obj='cobinhood'):
    """
    logger function
    """
    def decorator(func):
        def _wrapped(*args, **paras):
            coloredlogs.install(level=args[0].config.LOG_LEVEL, logger=LOG)

            if level == 'DEBUG':
                LOG.debug('%s fetch "%s"', obj, func.__name__)
            elif level == 'INFO':
                LOG.info('%s fetch "%s"', obj, func.__name__)
            return func(*args, **paras)
        return _wrapped
    return decorator
