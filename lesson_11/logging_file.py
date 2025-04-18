import logging

# Створення логера
logger = logging.getLogger("custom_logger")

# Налаштування рівня логування
logger.setLevel(logging.INFO)

# Створення обробника для запису в файл
file_handler = logging.FileHandler('logfile.txt')
#
# Налаштування рівня логування для обробника
file_handler.setLevel(logging.DEBUG)

# Створення форматера для обробника
formatter = logging.Formatter('%(name)s - %(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
#
# Додавання обробника до логера
logger.addHandler(file_handler)

# Логування подій
logger.debug('Це повідомлення рівня DEBUG')
logger.info('Це повідомлення рівня INFO')
logger.warning('Це повідомлення рівня WARNING')
logger.error('Це повідомлення рівня ERROR')
logger.critical('Це повідомлення рівня CRITICAL')

file_handler.close()