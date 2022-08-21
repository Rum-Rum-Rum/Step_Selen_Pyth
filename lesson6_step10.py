from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")

    input2 = browser.find_element(By.NAME, "email")
    input2.send_keys("PetVan@kuku.ru")

#   Задаём переменные
    # указывая директорию,где лежит файлу.txt
    # в конце должен быть /
    directory = "F:/1/"

    # имя файла, который будем загружать на сайт
    file_name = "123.txt"

    # собираем путь к файлу
    file_path = os.path.join(directory, file_name)

    print(directory)
    print(file_path)

# Ищем кнопку - "добавить файл"
    element = browser.find_element(By.ID, "file")

    # отправляем файл
    element.send_keys(file_path)

    # Нажать кнопку - "Выполнить"
    sub_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    sub_button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()