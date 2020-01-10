from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Firefox()
    browser.get(link)

    x = int(browser.find_element_by_id("num1").text) + int(
        browser.find_element_by_id("num2").text)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(x))
    button = browser.find_element_by_class_name("btn").click()

finally:
    time.sleep(10)
    browser.quit()
