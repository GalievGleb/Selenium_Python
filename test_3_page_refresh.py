from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\user\\Desktop\\PycharmProjects\\pythonselenium\\chromedriver.exe')#Указали директорию в которой находится хром драйвер, для того чтобы мы могли обращаться к браузеру гугл хром
base_url = 'https://www.saucedemo.com/'#совершенствуем код в переменную пихаем юрл который используем, удобно для ооп и для списков юрл
driver.get(base_url)#указываем url на который мы хотим заходить
driver.maximize_window()#открывается браузер на максимальный экран

login_standard_user = "standard_use"
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

warring_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warring_text = warring_text.text
assert value_warring_text == "Epic sadface: Username and password do not match any user in this service"
print("Good Test")

<<<<<<< HEAD
driver.refresh()
=======
driver.refresh()
>>>>>>> 25e35b307193c80b05dcfd28d6d2758aa064563f
