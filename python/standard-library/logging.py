import logging

# Basic Configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Logging messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# Custom Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('my_log.log')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Logging to the Custom Logger
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# Logging Exceptions
try:
    a = 1 / 0
except Exception as e:
    logging.error('An error occurred: %s', e, exc_info=True)

# Conditional Logging
if logging.getLogger().isEnabledFor(logging.DEBUG):
    logging.debug('This message will only be logged if DEBUG level is enabled')

# Rotating File Handler
from logging.handlers import RotatingFileHandler
rotating_handler = RotatingFileHandler('my_log.log', maxBytes=1000, backupCount=3)
rotating_handler.setLevel(logging.DEBUG)
rotating_handler.setFormatter(formatter)
logging.getLogger().addHandler(rotating_handler)
