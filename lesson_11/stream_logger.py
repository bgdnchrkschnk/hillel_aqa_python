import logging

# Створення логера
logger = logging.getLogger("console_logger")

# Налаштування рівня логування
logger.setLevel(logging.DEBUG)

# Створення обробника для виводу в stdout
console_handler = logging.StreamHandler()

# Налаштування рівня логування для обробника
console_handler.setLevel(logging.ERROR)

# Створення форматера для обробника
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Додавання обробника до логера
logger.addHandler(console_handler)

# # Логування подій
# logger.debug('Це повідомлення рівня DEBUG')
# logger.info('Це повідомлення рівня INFO')
# logger.warning('Це повідомлення рівня WARNING')
# logger.error('Це повідомлення рівня ERROR')
# logger.critical('Це повідомлення рівня CRITICAL')