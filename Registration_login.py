#############Registration_login:регистрация аккаунта аккаунта"

# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(7)
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# time.sleep(5)
# Email = driver.find_element_by_id("reg_email")
# Email.send_keys("test@gmail.ru")
# Password = driver.find_element_by_id("reg_password")
# Password.send_keys("HardPassword!@#!@#")
# time.sleep(3)
# Register_btn = driver.find_element_by_name("register")
# Register_btn.click()
# time.sleep(7)
# driver.quit()

######Registration_login:логин в систему систему

import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(7)
driver.get("https://practice.automationtesting.in/")
my_account = driver.find_element_by_link_text("My Account")
my_account.click()
time.sleep(5)
Email = driver.find_element_by_id("username")
Email.send_keys("test@gmail.ru")
Password = driver.find_element_by_id("password")
Password.send_keys("HardPassword!@#!@#")
time.sleep(3)
Login_btn = driver.find_element_by_name("login")
Login_btn.click()
time.sleep(7)
driver.quit()


