import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()

# открыть http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# нажать на My Account
driver.find_element_by_link_text("My Account").click()



# Тестирование функционала регистрации
# заполнить Email и Password в форме Register
driver.find_element_by_id("reg_email").send_keys("1@1.com")
driver.find_element_by_id("reg_password").send_keys("Ab<>123&456!=cD")
# нажать на Register: для валидации данных функционал сайта требует после заполнения полей
# сначала кликнуть в любое место кроме кнопки Register и сделать это не моментально
time.sleep(5)
ActionChains(driver).move_by_offset(100, 100).click().perform()
driver.find_element_by_name("register").click()



# Тестирование функционала логина
# заполнить Email и Password в форме Login
driver.find_element_by_id("username").send_keys("1@1.com")
driver.find_element_by_id("password").send_keys("Ab<>123&456!=cD")
# нажать на Login
driver.find_element_by_name("login").click()
# проверка, что присутствует кнопка Logout
logout = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ("//a[contains(text(), 'Logout')]"))))
assert logout
# выход из аккаунта
logout.click()

driver.quit()
