from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support. ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import pyautogui
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

# driver.get("https://demoqa.com/upload-download")
driver.get("https://gofile.io/uploadFiles")
driver.maximize_window()

# driver.find_element(By.ID, "uploadFile").send_keys("C:/Users/Ary Suta/Documents/LEWAT PINTU.pdf")

driver.find_element(By.XPATH, '//*[@id="rowUploadButton"]/div/div/div/div/div/div[1]/div/button').click()
time.sleep(3)
pyautogui.write(r"C:\Users\Ary Suta\Documents\LEWAT PINTU.pdf")
pyautogui.press("enter")
