import logging

# Створення логера
logger = logging.getLogger("logger_all")

# Налаштування рівня логування
logger.setLevel(logging.DEBUG)

# Створення обробника для виводу в stdout (консоль)
console_handler = logging.StreamHandler()

# Створення обробника для запису в файл
file_handler = logging.FileHandler('logs.log')

# Налаштування рівня логування для обробників
console_handler.setLevel(logging.ERROR)
file_handler.setLevel(logging.DEBUG)

# Створення форматера для обробників
formatter_console = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
formatter_file = logging.Formatter('%(filename)s - %(name)s - %(asctime)s - %(levelname)s - %(message)s')

# Налаштування форматера для обробників
console_handler.setFormatter(formatter_console)
file_handler.setFormatter(formatter_file)

# Додавання обробників до логера
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logging.shutdown()
# Логування подій
# logger.debug('Це повідомлення рівня DEBUG')
# logger.info('Це повідомлення рівня INFO')
# logger.warning('Це повідомлення рівня WARNING')
# logger.error('Це повідомлення рівня ERROR')
# logger.critical('Це повідомлення рівня CRITICAL')