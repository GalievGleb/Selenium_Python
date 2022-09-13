import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\user\\Desktop\\PycharmProjects\\pythonselenium\\chromedriver.exe')#Указали директорию в которой находится хром драйвер, для того чтобы мы могли обращаться к браузеру гугл хром
base_url = 'https://demoqa.com/radio-button'#совершенствуем код в переменную пихаем юрл который используем, удобно для ооп и для списков юрл
driver.get(base_url)#указываем url на который мы хотим заходить
driver.maximize_window()#открывается браузер на максимальный экран

# check_box = driver.find_element(By.XPATH, "//button[@aria-label='Toggle']") #обращение к элемену через id
# check_box.click()

radio_button = driver.find_element(By.XPATH, "//label[@for='yesRadio']") #обращаемся к элементу через тап по слову
radio_button.click()


