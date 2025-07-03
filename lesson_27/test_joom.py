from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestJoom:

    def test_joom_implicitly_wait(self, joom_driver):
        joom_driver.get("https://www.joom.com/")

        elements = joom_driver.find_elements(By.CSS_SELECTOR, "div.smallCards___tAHuQ")

        assert len(elements) == 2


    def test_joom_s(self, joom_driver):
        wait = WebDriverWait(joom_driver, 10)

        joom_driver.get("https://www.joom.com/")

        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.smallCards___tAHuQ")))

