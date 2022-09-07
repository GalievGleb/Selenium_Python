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
#text_products = driver.find_element(By.XPATH, "//span[@class='title']")#сохранили в переменную локатор, который сохраняет слово products
#value_text_products = text_products.text#метод текст считывает значение локатора(тоесть слово products). получается в этой переменной сохранили слово products
#print(value_text_products)
#assert value_text_products == "PRODUCTS"#производим сравнение
now_date = datetime.datetime.utcnow().strftime("%Y.№m.%d.%H.%M.%S")
name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot('C:\\Users\\user\\Desktop\\PycharmProjects\\pythonselenium\\screen\\' + name_screenshot)