from itertools import product

browsers = ['Chrome', 'Firefox']
oses = ['Windows', 'Linux']
versions = ['v1', 'v2']

for combo in product(browsers, oses, versions):
    print(f"Тестуємо: Браузер = {combo[0]}, ОС = {combo[1]}, Версія = {combo[2]}")




import pytest
from itertools import product

browsers = ['Chrome', 'Firefox']
oses = ['Windows', 'Linux']

# Генеруємо всі комбінації
params = list(product(oses, browsers))

@pytest.mark.parametrize("os_name, browser", params)
def test_app_compatibility(os_name, browser):
    print(f"\nТестуємо на: {os_name} + {browser}")
    assert isinstance(os_name, str)
    assert isinstance(browser, str)
