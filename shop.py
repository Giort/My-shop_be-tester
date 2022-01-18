from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


# открыть http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# логин в систему
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_id("username").send_keys("1@1.com")
driver.find_element_by_id("password").send_keys("Ab<>123&456!=cD")
driver.find_element_by_name("login").click()
# нажать на вкладку Shop
driver.find_element_by_link_text("Shop").click()



# Отображение страницы товара
# нажать на книгу HTML5 Forms
driver.find_element_by_xpath("//h3[contains(text(), 'HTML5 Forms')]").click()
# проверить, что заголовок книги называется HTML5 Forms
book_name = driver.find_element_by_css_selector(".product_title[itemprop='name']").text
assert book_name == "HTML5 Forms"



# Проверка количества товаров в категории
# открыть категорию HTML
driver.find_element_by_link_text("HTML").click()
# проверка, что в категории отображается три товара
items_count = driver.find_elements_by_css_selector("a>h3")
if len(items_count) == 3:
    print("\nOK: d категории 3 товара")
else:
    print("\nError: количество товаров в категории: " + str(len(items_count)))



# Сортировка товаров
# проверка, что в селекторе выбран вариант сортировки по умолчанию
sort = Select(driver.find_element_by_name("orderby"))
sort_text = sort.first_selected_option.text
assert sort_text == "Default sorting"
# выбор сортировки: по цене, от большей к меньшей
sort.select_by_value("price-desc")
sort = Select(driver.find_element_by_css_selector("select.orderby"))
# проверка, что в селекторе выбрана сортировка по цене от большей к меньшей
sort_value = sort.first_selected_option.get_attribute("value")
assert sort_value == "price-desc"



# Отображение, скидка товара
# открыть книгу Android Quick Start Guide
driver.find_element_by_xpath("//h3[contains(text(), 'Android Quick Start Guide')]").click()
# проверка, что содержимое старой цены = ₹600.00
old_price = driver.find_element_by_css_selector(".price > del > span").text
assert old_price == "₹600.00"
# проверка, что содержимое новой цены = ₹450.00
new_price = driver.find_element_by_css_selector(".price > ins > span").text
assert new_price == "₹450.00"
# открыть обложку книги
driver.find_element_by_css_selector(".images > a > img").click()
# закрыть окно предпросмотра
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))).click()



# Проверка цены в корзине
# добавление книги "HTML5 WebApp Development" в корзину
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button[data-product_id='182']"))).click()
# проверка, что возле иконки корзины указано количество товара "1 item"
# Если не установить ожидание, то текст считывается до того, как успеет обновиться
cart_text_1 = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'cartcontents'), '1 Item'))
assert cart_text_1 == True
# проверка, что возле иконки корзины указана стоимость "₹180.00"
cart_text_2 = driver.find_element_by_css_selector("a>.amount").text
assert cart_text_2 == "₹180.00"
# переход в корзину
driver.find_element_by_class_name("wpmenucart-contents").click()
# проверка, что в Subtotal отобразилась стоимость
subtotal_text = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, "//td[@data-title='Subtotal']"), "₹180.00"))
assert subtotal_text == True
# проверка, что в Total отобразилась стоимость
total_text = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, "//tr[@class='order-total']"), "₹189.00"))
assert total_text == True



# Работа в корзине
# нажать на вкладку Shop
driver.find_element_by_xpath("//a[contains(text(), 'Shop')]").click()
# скролл вниз на 300 пикселей
driver.execute_script("window.scrollBy(0, 300);")
# Добавление в корзину книг "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button[data-product_id='182']"))).click()
time.sleep(5)
driver.find_element_by_css_selector(".button[data-product_id='180']").click()
# переход в корзину
driver.find_element_by_class_name("wpmenucart-contents").click()
# удаление первой книги
time.sleep(3)
driver.find_elements_by_class_name("remove")[0].click()
# нажать Undo
WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.LINK_TEXT, "Undo?"))).click()
# В Quantity увеличить количество товара до 3 шт для "JS Data Structures and Algorithm"
qty = driver.find_element_by_css_selector("tr:nth-child(2)>td>div>input")
qty.clear()
qty.send_keys("3")
# нажать на кнопку Update Basket
driver.find_element_by_css_selector(".button[name='update_cart']").click()
# тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
qty_value = qty.get_attribute("value")
assert qty_value == "3"
# нажать на кнопку Apply Coupon
time.sleep(3)
driver.find_element_by_name("apply_coupon").click()
# проверить, что возникло сообщение Please enter a coupon code
ent_coupon = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//body"), "Please enter a coupon code."))
assert ent_coupon == True



# Покупка товара
# нажать на вкладку Shop
driver.find_element_by_xpath("//a[contains(text(), 'Shop')]").click()
# скролл вниз на 300 пикселей
driver.execute_script("window.scrollBy(0, 300);")
# добавление книги "HTML5 WebApp Development" в корзину
# не работает без time. Возможно, именно сейчас, в момент написания теста, есть какие-то задержки на сайте
time.sleep(3)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button[data-product_id='182']"))).click()
# переход в корзину
time.sleep(3)
cart = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "wpmenucart-contents")))
cart.click()
# нажать на кнопку Proceed to Checkout
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button"))).click()
# заполнение обязательных полей
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "billing_first_name"))).send_keys("Amayak")
driver.find_element_by_id("billing_last_name").send_keys("Akopyan")
driver.find_element_by_id("billing_email").send_keys("1@1.com")
driver.find_element_by_id("billing_phone").send_keys("2323232323")
# элемент выбора страны - не стандартный dropdown
driver.find_element_by_id("s2id_billing_country").click()
driver.find_element_by_id("s2id_autogen1_search").send_keys("Denmark")
ActionChains(driver).move_by_offset(0, 30).click().perform()
driver.find_element_by_id("billing_address_1").send_keys("Red Square, 1")
driver.find_element_by_id("billing_city").send_keys("Moscow")
# для полей Postcode и State нужно ожидание
postcode = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//p[@id='billing_postcode_field']/input")))
postcode.clear()
postcode.send_keys("109012")
town = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "billing_state")))
town.clear()
town.send_keys("Moscow")
# выбор способа оплаты: по чеку
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
driver.find_element_by_id("payment_method_cheque").click()
# нажать на кнопку Place Order
driver.find_element_by_id("place_order").click()
# проверка, что отобразилась надпись Thank you. Your order has been received.
thank = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "woocommerce-thankyou-order-received")))
thank_text = thank.text
assert thank_text == "Thank you. Your order has been received."

driver.quit()