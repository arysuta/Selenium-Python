from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


# driver.get("https://the-internet.herokuapp.com/login")

# driver.find_element(By.NAME, "username").send_keys("test123")
# # driver.find_element(By.LINK_TEXT, "Elemental Selenium").click()

# h2 = driver.find_elements(By.TAG_NAME, "h2")
# print(h2)

# link = driver.find_elements(By.TAG_NAME, "a")
# print(len(link))

# driver.find_element(By.CLASS_NAME, "radius").click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "button.radius").click()

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "#content > div > button").click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="elements"]/button').click()