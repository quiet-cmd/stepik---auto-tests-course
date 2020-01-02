from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    # browser = webdriver.Chrome()
    browser = webdriver.Firefox()
    browser.get(link)

    x = browser.find_element_by_tag_name("img")
    x = x.get_attribute("valuex")
    x = calc(x)
    input1 = browser.find_element_by_tag_name("input")
    input1 = input1.send_keys(x)

    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_css_selector('#robotsRule').click()
    browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # пустая строка ;3
