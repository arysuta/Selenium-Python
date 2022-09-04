from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demoqa.com/droppable")

elemen = driver.find_element(By.ID, "draggable")
kotak = driver.find_element(By.ID, "droppable")

action = ActionChains(driver)

action.drag_and_drop(elemen, kotak).perform()