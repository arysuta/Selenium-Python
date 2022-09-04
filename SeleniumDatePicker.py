from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import pyautogui

driver = webdriver.Chrome()


# driver.get("https://jqueryui.com/datepicker/")
driver.get("https://demoqa.com/date-picker")
driver.implicitly_wait(10)
driver.maximize_window()

# driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="content"]/iframe'))
# driver.find_element(By.ID, "datepicker").click()
# driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[5]/a').click()

# driver.find_element(By.ID, "datepicker").send_keys("11/11/2022")
# time.sleep(3)
# driver.find_element(By.ID, "datepicker").clear()

driver.find_element(By.ID, "datePickerMonthYearInput").click()
pyautogui.press('backspace',presses=10)
driver.find_element(By.ID, "datePickerMonthYearInput").send_keys("11/11/2022")

