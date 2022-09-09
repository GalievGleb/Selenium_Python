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
cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = cart_product_1.text
print(value_product_1)
"""хранит цену товара на главной странице"""
price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)
"""Добавление товара и переход в корзину"""
select_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("Select Product 1")

cart = driver.find_element(By.XPATH, "//div[@class='shopping_cart_container']")
cart.click()
print("Enter cart")

"""INFO Cart Product 1"""
"""хранит название товара в корзине и сравнивает с названием товара на главной странице"""
cart_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("INFO Cart Product 1 GOOD")
"""хранит название цены в корзине и сравнивает с ценой товара на главной странице"""
price_cart_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
value_cart_price_product_1 = price_cart_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print("INFO Cart Product 1 GOOD")

button_checout = driver.find_element(By.XPATH, "//button[@id='checkout']")
button_checout.click()
print("Click Checout")

"""Select User INFO"""
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys("Alex")
print("Input First Name")

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys("Ivanov")
print("Input Last Name")

zip = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip.send_keys("1234")
print("Input Zip")

button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print("Click Continue")

"""INFO Finish Product 1"""

"""хранит название товара в корзине и сравнивает с названием товара на главной странице"""
finish_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print("INFO finish Product 1 GOOD")

"""хранит название цены в корзине и сравнивает с ценой товара на главной странице"""
price_finish_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_finish_price_product_1 = price_finish_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1
print("INFO finish Product 1 GOOD")

summery_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]")
value_summery_price = summery_price.text
print(value_summery_price)
item_total = "Item total: " + value_finish_price_product_1
print(item_total)
assert value_summery_price == item_total
print("Total summary price Good")