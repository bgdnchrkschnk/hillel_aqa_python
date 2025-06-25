from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://example.com')

element = driver.find_element(By.ID, 'target-element')

# Скрол до елемента
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)



# Наприклад, координати X=0, Y=500
driver.execute_script("window.scrollTo(0, 500);")



# element coordinates
element = driver.find_element(By.ID, 'target-element')
location = element.location
x = location['x']
y = location['y']

driver.execute_script(f"window.scrollTo({x}, {y});")
