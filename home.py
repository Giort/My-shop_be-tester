from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()

# открыть http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# скролл вниз на 600
driver.execute_script("window.scrollBy(0, 600);")
# нажать на название Selenuim Ruby
driver.find_element_by_xpath("//h3[contains(text(), 'Selenium Ruby')]").click()
# нажать на вкладку Reviews
driver.find_element_by_xpath("//a[contains(text(), 'Reviews')]").click()
# поставить 5 звёзд
driver.find_element_by_class_name("star-5").click()
# в поле Review оставить комментарий "Nice book!"
driver.find_element_by_id("comment").send_keys("Nice book!")
# заполнить поля Name и Email
driver.find_element_by_id("author").send_keys("Tester")
driver.find_element_by_id("email").send_keys("1@1.com")
# нажать кнопку Submit
driver.find_element_by_id("submit").click()

driver.quit()
