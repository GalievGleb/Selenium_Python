import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\user\\Desktop\\PycharmProjects\\pythonselenium\\chromedriver.exe')#Указали директорию в которой находится хром драйвер, для того чтобы мы могли обращаться к браузеру гугл хром
base_url = 'http://automationpractice.com/index.php?id_category=3&controller=category#/'#совершенствуем код в переменную пихаем юрл который используем, удобно для ооп и для списков юрл
driver.get(base_url)#указываем url на который мы хотим заходить
driver.maximize_window()#открывается браузер на максимальный экран

action = ActionChains(driver)

price = driver.find_element(By.XPATH, "//div[@id='layered_price_slider']")
action.click_and_hold(price).move_by_offset(20, 0).release().perform() # вызвали метод с пм которого можно нажать, выбираем куда януть направо иль налево , отпускаем, сохраняем
print("Price +")
