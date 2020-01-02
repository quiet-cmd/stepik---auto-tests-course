from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Firefox()
    browser.get(link)

    x = int(browser.find_element_by_id("num1").text) + int(
        browser.find_element_by_id("num2").text)  # взяли и сложили 2 числа

    select = Select(browser.find_element_by_id("dropdown"))  # нашли список значений
    select.select_by_value(str(x))  # выбрали в нем значение x
    button = browser.find_element_by_class_name("btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # пустая строка ;3
