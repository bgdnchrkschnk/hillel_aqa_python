import logging

# Налаштування конфігурації логування
logging.basicConfig(filename='example.log', level=logging.DEBUG)

# Логування подій різного рівня (DEBUG, INFO, WARNING, ERROR, CRITICAL)
logging.debug('Це повідомлення рівня DEBUG') # 1
logging.info('Це повідомлення рівня INFO') # 2
logging.warning('Це повідомлення рівня WARNING') # 3
logging.error('Це повідомлення рівня ERROR') # 4
logging.critical('Це повідомлення рівня CRITICAL') # 5