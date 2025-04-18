# Set up colored console handler using colorlog
console_handler = colorlog.StreamHandler()
console_formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={'INFO': 'bold_cyan'}
)
console_handler.setFormatter(console_formatter)
console_handler.setLevel(logging.INFO)  # Set level for console handler

# Set up file handler
file_handler = logging.FileHandler(filename='test_logs.log', encoding='utf-8')
file_formatter = logging.Formatter('%(message)s')
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.INFO)  # Set level for file handler

custom_logger = logging.getLogger(request.function.__name__)