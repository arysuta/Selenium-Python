from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#alertButton").click()
time.sleep(2)
driver.switch_to.alert.accept()

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#confirmButton").click()
time.sleep(2)
driver.switch_to.alert.dismiss()

time.sleep(2)
element = driver.find_element(By.CSS_SELECTOR, "#promtButton")
driver.execute_script("arguments[0].click();", element)
# driver.find_element(By.CSS_SELECTOR, "#promtButton").click()
time.sleep(2)
driver.switch_to.alert.send_keys("Belajar testing")
time.sleep(2)
driver.switch_to.alert.accept()