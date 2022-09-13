import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\user\\Desktop\\PycharmProjects\\pythonselenium\\chromedriver.exe')#Указали директорию в которой находится хром драйвер, для того чтобы мы могли обращаться к браузеру гугл хром
base_url = 'https://demoqa.com/buttons'#совершенствуем код в переменную пихаем юрл который используем, удобно для ооп и для списков юрл
driver.get(base_url)#указываем url на который мы хотим заходить
driver.maximize_window()#открывается браузер на максимальный экран

# check_box = driver.find_element(By.XPATH, "//button[@aria-label='Toggle']") #обращение к элемену через id
# check_box.click()

action = ActionChains(driver) #создали переменную action в которой экземпляром класса является ActionChains в которую мы передаем драйвер = переменную которая хранит веб драйвер хром
double = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']") #локатор кнопки
action.double_click(double).perform()  # обращаемся к переменной чтобы произвести дабл клик перформ метод сохраняет действие

right_click = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']") #локатор кнопки
action.context_click(right_click).perform()

