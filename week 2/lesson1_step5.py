from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Firefox()
    browser.get(link)

    x = browser.find_element_by_id("input_value")  # нашли тег с нашим числом
    x = x.text  # взяли число х
    x = calc(x)  # вставили х в формулу
    input1 = browser.find_element_by_tag_name("input")  # нашли поле ввода
    input1 = input1.send_keys(x)  # вввели в поле ввода наше число
    browser.find_element_by_id("robotCheckbox").click()

    browser.find_element_by_css_selector('#robotsRule').click()
    browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # пустая строка ;3
