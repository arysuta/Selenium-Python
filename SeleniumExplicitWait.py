from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()

driver.get("https://demoqa.com/alerts")

driver.find_element(By.CSS_SELECTOR, "#timerAlertButton").click()


try:
    WebDriverWait(driver,10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    print("Alert di pencet")

except TimeoutException:
    print("Alert tidak muncul")
    pass
