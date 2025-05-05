import logging


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        force=True,
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)
import pytest

def test_log_success():
    username = "Oksana"
    status = "success"
    log_event(username=username, status=status)
    with open("login_system.log", "r") as file:
        log_contents = file.read()

    assert f"Login event - Username: {username}, Status: {status}" in log_contents


def test_log_expired():
    username = "Oksana"
    status = "expired"
    log_event(username=username, status=status)
    with open("login_system.log", "r") as file:
        log_contents = file.read()

    assert f"Login event - Username: {username}, Status: {status}" in log_contents

def test_log_failed():
    username = "Oksana"
    status = "failed"
    log_event(username=username, status=status)
    with open("login_system.log", "r") as file:
        log_contents = file.read()

    assert f"Login event - Username: {username}, Status: {status}" in log_contents