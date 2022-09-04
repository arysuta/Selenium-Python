from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time
import pyautogui

pilih = webdriver.ChromeOptions()
pilih.headless = True

driver = webdriver.Chrome(options=pilih)
driver.get("https://demoqa.com")
print(driver.title)
