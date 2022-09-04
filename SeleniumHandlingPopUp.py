from sqlite3 import Time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()

for i in range (2):
    driver.get("https://tees.co.id/")

    try:
        WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, "/html/body/div[1]")))
        print("pop up muncul")
        driver.find_element(By.CLASS_NAME, "btn-modal-close").click()
        print("pop up closed")

    except TimeoutException:
        print("pop up tidak muncul")
        pass

    time.sleep(3)