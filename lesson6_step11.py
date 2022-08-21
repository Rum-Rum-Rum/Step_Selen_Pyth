from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from math import log, sin

#lesson6_step4.py
def calc(x):
    return str(log(abs(12 * sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()

    # Принять confirm
    alert = browser.switch_to.alert
    alert.accept()

    # Посчитали значение
    x = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap").text
    print(x)
    y = calc(x)
    print(y)

    # Подставить значение y
    answer = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    answer.send_keys(y)

    # Нажать кнопку - "Выполнить"
    sub_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    sub_button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()