import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\user\\Desktop\\PycharmProjects\\pythonselenium\\chromedriver.exe')#Указали директорию в которой находится хром драйвер, для того чтобы мы могли обращаться к браузеру гугл хром
base_url = 'https://demoqa.com/date-picker'#совершенствуем код в переменную пихаем юрл который используем, удобно для ооп и для списков юрл
driver.get(base_url)#указываем url на который мы хотим заходить
driver.maximize_window()#открывается браузер на максимальный экран

# check_box = driver.find_element(By.XPATH, "//button[@aria-label='Toggle']") #обращение к элемену через id
# check_box.click()

new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
new_date.click()
time.sleep(5)
date_17 = driver.find_element(By.XPATH, "//div[@aria-label='Choose Friday, September 16th, 2022']")
date_17.click()