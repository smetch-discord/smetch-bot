import logging


def log_setup():
    """
    Sets up basic logging
    """
    __name__ = 'log_setup'
    logging.basicConfig(
        filename='bot.log',
        filemode='w',
        format='%(name)s: %(levelname)s - %(message)s',
        level=logging.DEBUG
    )
    log = logging.getLogger(__name__)
    log.info('Logging has been successfully set up')
    discord_log = logging.getLogger("discord")
    asyncio_log = logging.getLogger("asyncio")
    discord_log.setLevel(logging.WARNING)
    asyncio_log.setLevel(logging.WARNING)


log_setup()
