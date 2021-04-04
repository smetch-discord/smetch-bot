import logging


def log_setup():
    __name__ = 'log_setup'
    logging.basicConfig(
        filename='bot.log',
        filemode='w',
        format='%(name)s: %(levelname)s - %(message)s',
        level=logging.DEBUG
    )
    log = logging.getLogger(__name__)
    log.info('Logging has been successfully set up')
