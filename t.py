import logging
import pytest

"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

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
        format='%(asctime)s - %(message)s'
    )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)



@pytest.fixture(autouse=True)
def capture_logs(caplog):
    """Автоматически перенастраивает логгер 'log_event' на запись в caplog,
    чтобы не писать в файл."""
    caplog.set_level(logging.DEBUG, logger="log_event")
    yield


def test_log_event_success(caplog):
    log_event("alice", "success")
    records = [r for r in caplog.records if r.name == "log_event"]
    assert len(records) == 1
    assert records[0].levelno == logging.INFO
    assert "Username: alice, Status: success" in records[0].getMessage()


def test_log_event_expired(caplog):
    log_event("david", "expired")
    records = [r for r in caplog.records if r.name == "log_event"]
    assert len(records) == 1
    assert records[0].levelno == logging.WARNING
    assert "Username: david, Status: expired" in records[0].getMessage()


def test_log_event_failed(caplog):
    log_event("vlad", "failed")
    records = [r for r in caplog.records if r.name == "log_event"]
    assert len(records) == 1
    assert records[0].levelno == logging.ERROR
    assert "Username: vlad, Status: failed" in records[0].getMessage()


def test_log_event_unknown_status(caplog):
    log_event("eve", "online")
    records = [r for r in caplog.records if r.name == "log_event"]
    assert len(records) == 1
    assert records[0].levelno == logging.ERROR
    assert "Username: eve, Status: online" in records[0].getMessage()