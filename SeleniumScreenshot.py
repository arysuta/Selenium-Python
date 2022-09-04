from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyautogui

pilih = webdriver.ChromeOptions()
pilih.add_experimental_option('excludeSwitches', ['enable-logging'])
pilih.headless = True
pilih.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=pilih)
driver.get("https://demoqa.com")
print(driver.title)
driver.get_screenshot_as_file("screenshot_selenium2.png")