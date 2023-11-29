#####Shop: отображение страницы товара товара

# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(7)
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# time.sleep(5)
# Email = driver.find_element_by_id("username")
# Email.send_keys("test@gmail.ru")
# Password = driver.find_element_by_id("password")
# Password.send_keys("HardPassword!@#!@#")
# time.sleep(3)
# Login_btn = driver.find_element_by_name("login")
# Login_btn.click()
# time.sleep(7)
# Shop = driver.find_element_by_link_text("Shop")
# Shop.click()
# HTML5book = driver.find_element_by_css_selector(".post-181 h3")
# HTML5book.click()
# time.sleep(3)
# Zagolovok = driver.find_element_by_css_selector(".summary h1")
# Zagolovok_text = Zagolovok.text
# assert Zagolovok_text == "HTML5 Forms"
# time.sleep(3)
# driver.quit()

#####Shop: количество товаров в категории категории

# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(7)
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# time.sleep(5)
# Email = driver.find_element_by_id("username")
# Email.send_keys("test@gmail.ru")
# Password = driver.find_element_by_id("password")
# Password.send_keys("HardPassword!@#!@#")
# time.sleep(3)
# Login_btn = driver.find_element_by_name("login")
# Login_btn.click()
# time.sleep(7)
# Shop = driver.find_element_by_link_text("Shop")
# Shop.click()
# time.sleep(5)
# HTML_btn = driver.find_element_by_css_selector(".product-categories :nth-child(2) a")
# HTML_btn.click()
# time.sleep(5)
# items = driver.find_elements_by_css_selector(".products .button")
# if len(items) == 3:
#     print("Во вкладке 3 товара")
# else:
#     print("Ошибка. Количество товаров: " + str(len(items)))
# time.sleep(5)
# driver.quit()

#####Shop: сортировка товаров

# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(7)
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# time.sleep(5)
# Email = driver.find_element_by_id("username")
# Email.send_keys("test@gmail.ru")
# Password = driver.find_element_by_id("password")
# Password.send_keys("HardPassword!@#!@#")
# time.sleep(3)
# Login_btn = driver.find_element_by_name("login")
# Login_btn.click()
# time.sleep(7)
# Shop = driver.find_element_by_link_text("Shop")
# Shop.click()
# time.sleep(5)
# Cortirovka = driver.find_element_by_css_selector(".orderby")
# Cortirovka_check = Cortirovka.get_attribute("value")
# print("value of Cortirovka: ", Cortirovka_check)
# if Cortirovka_check == "menu_order":
#     print("Стоит сортировка по умолчание")
# else:
#     print("Стоит другой атрибут")
# time.sleep(5)
# element = driver.find_element_by_css_selector(".orderby")
# select =Select(element)
# select.select_by_value("price-desc")
# time.sleep(5)
# Cortirovka2 = driver.find_element_by_css_selector(".orderby")
# Cortirovka_check2 = Cortirovka2.get_attribute("value")
# print("value of Cortirovka2: ", Cortirovka_check2)
# if Cortirovka_check2 == "price-desc":
#     print("Стоит сортировка по цене от большей к меньшему")
# else:
#     print("Стоит другой атрибут")
# time.sleep(5)
# driver.quit()


#####Shop: отображение, скидка товара товара

# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(7)
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# time.sleep(5)
# Email = driver.find_element_by_id("username")
# Email.send_keys("test@gmail.ru")
# Password = driver.find_element_by_id("password")
# Password.send_keys("HardPassword!@#!@#")
# time.sleep(3)
# Login_btn = driver.find_element_by_name("login")
# Login_btn.click()
# time.sleep(7)
# Shop = driver.find_element_by_link_text("Shop")
# Shop.click()
# time.sleep(5)
# android_book = driver.find_element_by_css_selector(".post-169 h3")
# android_book.click()
# oldprice = driver.find_element_by_css_selector(".price > del > span")
# oldprice_text = oldprice.text
# newprice = driver.find_element_by_css_selector(".price > ins > span")
# newprice_text = newprice.text
# assert oldprice_text == "₹600.00"
# assert newprice_text == "₹450.00"
# oblozhka = WebDriverWait(driver,10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# oblozhka.click()
# time.sleep(5)
# oblozhka_close = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# oblozhka_close.click()
# time.sleep(5)
# driver.quit()


########shop проверка цены в корзине

# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(7)
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# time.sleep(5)
# Email = driver.find_element_by_id("username")
# Email.send_keys("test@gmail.ru")
# Password = driver.find_element_by_id("password")
# Password.send_keys("HardPassword!@#!@#")
# time.sleep(3)
# Login_btn = driver.find_element_by_name("login")
# Login_btn.click()
# time.sleep(7)
# Shop = driver.find_element_by_link_text("Shop")
# Shop.click()
# time.sleep(5)
# Add_to_basket = driver.find_element_by_css_selector(".products .post-182 .button")
# Add_to_basket.click()
# time.sleep(5)
# prise = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
# prise_text = prise.text
# item = driver.find_element_by_css_selector(".cartcontents")
# item_text = item.text
# assert prise_text == "₹180.00"
# assert item_text == "1 Item"
# corzina = driver.find_element_by_css_selector(".wpmenucart-contents")
# corzina.click()
# subtotal = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal td"), "₹180.00"))
# total = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total td"), "₹183.60"))
# driver.quit()

########Shop работа в корзине корзине


# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(7)
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# time.sleep(5)
# Email = driver.find_element_by_id("username")
# Email.send_keys("test@gmail.ru")
# Password = driver.find_element_by_id("password")
# Password.send_keys("HardPassword!@#!@#")
# time.sleep(3)
# Login_btn = driver.find_element_by_name("login")
# Login_btn.click()
# time.sleep(7)
# Shop = driver.find_element_by_link_text("Shop")
# Shop.click()
# time.sleep(5)
# driver.execute_script("window.scrollBy(0, 300);")
# time.sleep(5)
# Add_to_basket = driver.find_element_by_css_selector(".products .post-182 .button")
# Add_to_basket.click()
# time.sleep(5)
# Add_to_basket2 = driver.find_element_by_css_selector(".products .post-180 .button")
# Add_to_basket2.click()
# corzina = driver.find_element_by_css_selector(".wpmenucart-contents")
# corzina.click()
# time.sleep(3)
# Close = driver.find_element_by_css_selector('[data-product_id="182"]')
# Close.click()
# time.sleep(3)
# Undo = driver.find_element_by_link_text("Undo?")
# Undo.click()
# Quantity = driver.find_element_by_css_selector('[name = "cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
# Quantity.clear()
# time.sleep(3)
# Quantity2 = driver.find_element_by_css_selector('[name = "cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
# Quantity2.send_keys(3)
# time.sleep(3)
# UPDATE_BASKET = driver.find_element_by_name("update_cart")
# UPDATE_BASKET.click()
# time.sleep(3)
# Quantity_check = driver.find_element_by_css_selector('[name = "cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
# Quantity_check_text = Quantity_check.get_attribute("value")
# assert Quantity_check_text == "3"
# time.sleep(3)
# APPLY_COUPON = driver.find_element_by_name("apply_coupon")
# APPLY_COUPON.click()
# time.sleep(3)
# Baloon = driver.find_element_by_css_selector(".woocommerce-error li")
# Baloon_text = Baloon.text
# assert Baloon_text == "Please enter a coupon code."
# driver.quit()


#######Shop покупка товара товара

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(7)
driver.get("https://practice.automationtesting.in/")
Shop = driver.find_element_by_link_text("Shop")
Shop.click()
time.sleep(5)
driver.execute_script("window.scrollBy(0, 300);")
Add_to_basket = driver.find_element_by_css_selector(".products .post-182 .button")
Add_to_basket.click()
time.sleep(3)
corzina = driver.find_element_by_css_selector(".wpmenucart-contents")
corzina.click()
time.sleep(3)
wait = WebDriverWait(driver, 10)
PROCEED_TO_CHECKOUT_wait = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".checkout-button")))
PROCEED_TO_CHECKOUT = driver.find_element_by_css_selector(".checkout-button")
PROCEED_TO_CHECKOUT.click()
time.sleep(3)
First_name_wait = wait.until(EC.element_to_be_clickable((By.ID,"billing_first_name")))
First_name = driver.find_element_by_id("billing_first_name")
First_name.send_keys("Dima")
Last_name = driver.find_element_by_id("billing_last_name")
Last_name.send_keys("Kopaev")
Email_address = driver.find_element_by_id("billing_email")
Email_address.send_keys("Test@gmail.com")
Phone = driver.find_element_by_id("billing_phone")
Phone.send_keys("123123123132")
time.sleep(3)
Country_click = driver.find_element_by_css_selector(".select2-choice")
Country_click.click()
time.sleep(3)
Country_input = driver.find_element_by_id("s2id_autogen1_search")
Country_input.send_keys("Russia")
time.sleep(3)
Country_choose = driver.find_element_by_css_selector(".select2-result-label")
Country_choose.click()
time.sleep(3)
Address = driver.find_element_by_id("billing_address_1")
Address.send_keys("Pushkina")
Town = driver.find_element_by_id("billing_city")
Town.send_keys("Saint-Petersburg")
State = driver.find_element_by_id("billing_state")
State.send_keys("center")
Postcode = driver.find_element_by_id("billing_postcode")
Postcode.send_keys("444")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
Check_payments = driver.find_element_by_id("payment_method_cheque")
Check_payments.click()
time.sleep(3)
Place_order = driver.find_element_by_id("place_order")
Place_order.click()
time.sleep(3)
Nadpis = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".woocommerce-thankyou-order-received"),"Thank you. Your order has been received."))
time.sleep(3)
Nadpis2 = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".woocommerce-thankyou-order-details .method"),"Check Payments"))
driver.quit()

