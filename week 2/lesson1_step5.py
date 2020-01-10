from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Firefox()
    browser.get(link)

    x = browser.find_element_by_id("input_value")
    x = x.text
    x = calc(x)
    input1 = browser.find_element_by_tag_name("input")
    input1 = input1.send_keys(x)
    browser.find_element_by_id("robotCheckbox").click()

    browser.find_element_by_css_selector('#robotsRule').click()
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
