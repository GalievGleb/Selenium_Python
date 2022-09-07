import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\user\\Desktop\\PycharmProjects\\pythonselenium\\chromedriver.exe')#Указали директорию в которой находится хром драйвер, для того чтобы мы могли обращаться к браузеру гугл хром
base_url = 'https://www.saucedemo.com/'#совершенствуем код в переменную пихаем юрл который используем, удобно для ооп и для списков юрл
driver.get(base_url)#указываем url на который мы хотим заходить
driver.maximize_window()#открывается браузер на максимальный экран

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.ID, "user-name") #обращение к элемену через id
user_name.send_keys(login_standard_user)#спрятанный standard_user
print("Input Login")

password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys(password_all)
print("Input Password")
password.send_keys(Keys.RETURN)#команда enter
filter = driver.find_element(By.XPATH, "//select[@data-test='product_sort_container']")#выбираем кнопку фильтр
filter.click()#делаем тап по фильтру
print("Click filter")
filter.send_keys(Keys.DOWN)#на кнопку ниже
filter.send_keys(Keys.RETURN)#enter
