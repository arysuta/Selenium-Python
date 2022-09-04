from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import pyautogui
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demoqa.com/select-menu")

# old style

# pilih = Select(driver.find_element(By.ID, "oldSelectMenu"))
# pilih.select_by_visible_text("Yellow")
# pilih.select_by_value("4")

#new style

driver.find_element(By.ID, "selectOne").click()
time.sleep(2)
pyautogui.typewrite('Prof.')
time.sleep(2)
pyautogui.press('Enter')
time.sleep(3)
driver.execute_script("window.scrollTo(0,300)")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#selectMenuContainer > div:nth-child(7) > div > div > div > div.css-1wy0on6 > div').click()
time.sleep(2)
pyautogui.typewrite('Green')
time.sleep(2)
pyautogui.press('Enter')
time.sleep(2)
pyautogui.typewrite('Blue')
time.sleep(2)
pyautogui.press('Enter')



