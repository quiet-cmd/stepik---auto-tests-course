from selenium import webdriver
from selenium.webdriver.support.ui import Select
from math import log, sin
import time

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Firefox()
    browser.get(link)

    x = int(browser.find_element_by_id("input_value").text)
    x = str(log(abs(12 * sin(x))))
    input1 = browser.find_element_by_id("answer").send_keys(x)

    check = browser.find_element_by_id("robotCheckbox").click()
    radio = browser.find_element_by_id("robotsRule")

    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    button = browser.find_element_by_tag_name("button").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # пустая строка ;3
