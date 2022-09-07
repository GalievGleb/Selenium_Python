import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# driver хранит наш веб драйвер
driver = webdriver.Chrome(executable_path='C:\\Users\\user\\Desktop\\PycharmProjects\\pythonselenium\\chromedriver.exe')#Указали директорию в которой находится хром драйвер, для того чтобы мы могли обращаться к браузеру гугл хром
driver.get('https://www.saucedemo.com/')# указываем url на который мы хотим заходить
driver.maximize_window()# открывается браузер на максимальный экран
#user_name = driver.find_element_by_id("user-name")
user_name = driver.find_element(By.ID, "user-name") #обращение к элемену через id
user_name.send_keys("standard_user")
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("secret_sauce")
button_login = driver.find_element(By.XPATH, "//input[@value='Login']")
button_login.click()
#time.sleep(10) #заморозка времени в секундах
#driver.close() #закрытие браузера