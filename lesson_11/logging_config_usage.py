import logging
import logging.config

logging.config.fileConfig('logging_config.ini')

# Використання логера
logger = logging.getLogger('sampleLogger')

logger.debug('Це повідомлення рівня DEBUG')
logger.info('Це повідомлення рівня INFO')