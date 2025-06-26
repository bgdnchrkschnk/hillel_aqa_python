import logging
import sys
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lesson_11.stream_logger import logger

class TestSeleniumExamples:

    def test_find_element_for_login(self, selenium_driver_demo):

        # Знаходження елемента за XPath
        user_name: WebElement = selenium_driver_demo.find_element(By.XPATH, "//input[@id='username']")
        password: WebElement = selenium_driver_demo.find_element(By.XPATH, "//input[@id='password']")
        login: WebElement = selenium_driver_demo.find_element(By.XPATH, "//button[@id='login_button']")

        # Знаходження елемента за CSS класом
        selenium_driver_demo.find_element(By.CSS_SELECTOR, ".input-field#username")
        selenium_driver_demo.find_element(By.CSS_SELECTOR, ".input-field#password")
        selenium_driver_demo.find_element(By.CSS_SELECTOR, "#login_button")

        assert user_name.is_displayed()
        assert password.is_displayed()
        assert login.is_displayed()


    def test_find_elements_for_logout(self, selenium_driver_demo):

        # Знаходження елементів за XPath
        list_elements_xpath: list[WebElement] = selenium_driver_demo.find_elements(By.XPATH, "//li")

        # Знаходження елемента за CSS класом
        list_elements_css: list[WebElement] = selenium_driver_demo.find_elements(By.CSS_SELECTOR, "li")

        assert len(list_elements_xpath) == 3
        assert len(list_elements_css) == 3


        for element in list_elements_xpath:
            assert "Елемент списку " in element.text

    def test_submit_form(self, selenium_driver_elements):

        logger.info("TEST")

        # Знаходження текстових полів за ID і введення тексту
        username_field: WebElement = selenium_driver_elements.find_element(By.CSS_SELECTOR, "#username")
        username_field.send_keys("example_username")

        password_field = selenium_driver_elements.find_element(By.CSS_SELECTOR, "#password")
        password_field.send_keys("example_password")

        # Знаходження радіо кнопок за ID і вибір варіанта
        male_radio = selenium_driver_elements.find_element(By.CSS_SELECTOR, "#male")
        male_radio.click()

        # Знаходження чекбоксу за ID і встановлення прапорця
        newsletter_checkbox = selenium_driver_elements.find_element(By.CSS_SELECTOR, "#newsletter")
        newsletter_checkbox.click()

        # Вибір значення з випадаючого списку за ID
        country_dropdown = Select(selenium_driver_elements.find_element(By.CSS_SELECTOR, "#country"))
        country_dropdown.select_by_visible_text("США")

        # Натискання на кнопку за ID
        submit_button = selenium_driver_elements.find_element(By.CSS_SELECTOR, "#submit")
        submit_button.click()

    def test_iframe(self, selenium_driver_elements):
        selenium_driver_elements.get("https://demo.automationtesting.in/Frames.html")
        # Перемикаємося до фрейму
        iframe: WebElement = selenium_driver_elements.find_element(By.CSS_SELECTOR, "#singleframe")

        selenium_driver_elements.switch_to.frame(iframe)
        input: WebElement = selenium_driver_elements.find_element(By.CSS_SELECTOR, "input")

        input.send_keys("Some password...")

        time.sleep(2)

    def test_scrolling(self, selenium_driver_scroll):
        selenium_driver_scroll.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(2)

    def test_scrolling_2(self, selenium_driver_scroll):
        selenium_driver_scroll.get("https://demo.automationtesting.in/Register.html")

        footer: WebElement = selenium_driver_scroll.find_element(By.CSS_SELECTOR, "footer")

        # Скрол до елемента
        selenium_driver_scroll.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", footer)

        time.sleep(5)

    def test_alerts(self, selenium_driver_alerts):
        # Показати Alert і отримати текст з нього
        selenium_driver_alerts.find_element(By.CSS_SELECTOR, ".btn.btn-danger").click()
        alert = Alert(selenium_driver_alerts)
        logger.info(f"TEXT Alert: {alert.text}")
        alert.dismiss()

        time.sleep(1)

        selenium_driver_alerts.find_element(By.CSS_SELECTOR, "a[href='#CancelTab']").click()

        # Показати Confirm і підтвердити його
        selenium_driver_alerts.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
        alert = Alert(selenium_driver_alerts)
        logger.info(f"Текст Confirm: {alert.text}")
        alert.accept()

        time.sleep(1)

        selenium_driver_alerts.find_element(By.CSS_SELECTOR, "a[href='#Textbox']").click()

        # Показати Prompt, ввести текст і підтвердити його
        selenium_driver_alerts.find_element(By.CSS_SELECTOR, ".btn.btn-info").click()
        alert = Alert(selenium_driver_alerts)
        print("Текст Prompt:", alert.text)
        alert.send_keys("some text...")
        time.sleep(2)
        alert.accept()

    def test_actions(self, selenium_driver_alerts):
        # відкриваємо сторінку з прикладом
        driver = selenium_driver_alerts
        driver.get("http://localhost:8000/action_chains.html")

        # знаходимо eлемент circle
        circle = driver.find_element(By.ID, "circle")

        # cтворюємо екземпляр класу ActionChains
        actions = ActionChains(driver)

        # отримаємо розміри зони, де ми можемо переміщувати коло
        zone = driver.find_element(By.ID, "container")

        # дозволена довжина/ширина зони для руху
        azw = zone.size['width'] - circle.size['width'] - 10
        azh = zone.size['height'] - circle.size['height'] - 10

        try:
            # центр зони
            actions.click_and_hold(circle).move_to_element(zone).perform()
            time.sleep(1)
            # правий нижнiй кут
            actions.move_to_element(circle).move_by_offset(azw / 2, azh / 2).perform()
            time.sleep(1)
            # правий верхнiй кут
            actions.move_to_element(circle).move_by_offset(0, -azh).perform()
            time.sleep(1)
            # лiвий верхнiй кут
            actions.move_to_element(circle).move_by_offset(-azw, 0).perform()
            time.sleep(1)
            # лiвий  нижнiй кут
            actions.move_to_element(circle).move_by_offset(0, azh).perform()
            time.sleep(1)
            # центр зони
            actions.click_and_hold(circle).move_to_element(zone).perform()
            time.sleep(1)
            # подвiйний клiк
            actions.double_click(circle).perform()
            time.sleep(1)
            # одинарний клiк
            actions.click(circle).perform()
            time.sleep(1)

            # перевіряємо чи змінився фоновий колір на зелений
            background_color = circle.value_of_css_property("background-color")
            # RGBA значення кольору зеленого (0, 128, 0)
            # з повним непрозорістю (alpha = 1)
            if background_color == "rgba(0, 128, 0, 1)":
                print("Фон змінився на зелений!")

            # курсор поза межi circle
            actions.move_by_offset(-100, -100).perform()
            time.sleep(1)

            # перевіряємо чи змінився фоновий колір на червоний
            background_color_out = circle.value_of_css_property("background-color")
            # RGBA значення кольору зеленого (255, 0, 0)
            # з повним непрозорістю (alpha = 1)
            if background_color_out == "rgba(255, 0, 0, 1)":
                print("Фон змінився на червоний!")

            # натискання клавіші Enter
            actions.send_keys(Keys.ENTER).perform()
            time.sleep(1)
            alert = Alert(driver)
            # закриваємо Confirm вiкно
            alert.accept()
            time.sleep(0.5)
        finally:
            logger.error(f"Something went wrong: {driver}")

    def test_move_ot_dropdown(self, selenium_driver_alerts):
        driver = selenium_driver_alerts
        driver.get("http://localhost:8000/drop_down_menu.html")
        actions = ActionChains(driver)

        # знайти кнопку "Menu"
        time.sleep(1)
        menu_button = driver.find_element(By.TAG_NAME, "button")

        # навести курсор на кнопку "Menu", щоб відобразити випадаюче меню
        actions.move_to_element(menu_button).perform()

        # знайти всі посилання на продукти в меню "Products"
        product_links = driver.find_elements(By.CSS_SELECTOR, ".dropdown-submenu .dropdown-content .product-link")

        # пройтися по кожному посиланню і натиснути його
        for link in product_links:
            actions.move_to_element(link).perform()
            actions.click(link).perform()
            time.sleep(1)
            # почекати, поки з'явиться діалогове вікно підтвердження
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            time.sleep(1)
            # підтвердити діалогове вікно
            alert = driver.switch_to.alert
            alert.accept()









