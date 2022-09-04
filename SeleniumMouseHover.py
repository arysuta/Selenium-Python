from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://demoqa.com/menu")
driver.maximize_window()
driver.implicitly_wait(10)

#cara1
# menu = driver.find_element(By.LINK_TEXT, "Main Item 2")
# hover = ActionChains(driver).move_to_element(menu)
# hover.perform()

#cara2

ActionChains(driver).move_to_element((driver.find_element(By.LINK_TEXT, "Main Item 2"))).perform()
ActionChains(driver).move_to_element((driver.find_element(By.LINK_TEXT, "SUB SUB LIST »"))).perform()