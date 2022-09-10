import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\user\\Desktop\\PycharmProjects\\pythonselenium\\chromedriver.exe')#Указали директорию в которой находится хром драйвер, для того чтобы мы могли обращаться к браузеру гугл хром
base_url = 'https://www.saucedemo.com/'#совершенствуем код в переменную пихаем юрл который используем, удобно для ооп и для списков юрл
driver.get(base_url)#указываем url на который мы хотим заходить
driver.maximize_window()#открывается браузер на максимальный экран

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.ID, "user-name") #обращение к элемену через id
user_name.send_keys(login_standard_user)
print("Input Login")
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys(password_all)
print("Input Password")
button_login = driver.find_element(By.XPATH, "//input[@value='Login']")
button_login.click()
print("Click Login Button")

"""INFO Product #1"""
"""хранит название товара на главной странице"""
cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
value_product_1 = cart_product_1.text
print(value_product_1 + " - Название первого товара")
"""хранит цену товара на главной странице"""
price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1 + " - Цена первого товара")

"""INFO Product #2"""
"""хранит название товара на главной странице"""
cart_product_2 = driver.find_element(By.XPATH, "//*[@id='item_5_title_link']/div")
value_product_2 = cart_product_2.text
print(value_product_2 + " - Название второго товара")
"""хранит цену товара на главной странице"""
price_product_2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div")
value_price_product_2 = price_product_2.text
print(value_price_product_2 + " - Цена второго товара")

"""Тапаем на кнопку 'ADD TO CART'"""
button_add_to_cart_1 = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']")
button_add_to_cart_1.click()
print("Первый товар добавили в корзину")

button_add_to_cart_2 = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']")
button_add_to_cart_2.click()
print("Второй товар добавили в корзину")

cart = driver.find_element(By.XPATH, "//div[@class='shopping_cart_container']")
cart.click()
print("Enter cart")

button_checout = driver.find_element(By.XPATH, "//button[@id='checkout']")
button_checout.click()
print("Click Checout")

"""Select User INFO"""
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys("Gleb")
print("Input First Name")

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys("Galiev")
print("Input Last Name")

zip = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip.send_keys("666")
print("Input Zip")

button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print("Click Continue")

"""Сравниваем цену которая была в главном меню с ценой товаров которая у нас выходит перед оплатой"""

summ_price_orig = value_price_product_2 + value_price_product_1
print(summ_price_orig)

summery_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]")
value_summery_price = summery_price.text
print(value_summery_price)

