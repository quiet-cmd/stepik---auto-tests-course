from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin
import time

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Firefox()
    browser.get(link)
    # говорим WebDriver искать каждый элемент в течение 5 секунд browser.implicitly_wait(5)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element_by_id("book").click()
    x = browser.find_element_by_id("input_value").text
    x = str(log(abs(12 * sin(int(x)))))
    input1 = browser.find_element_by_id("answer").send_keys(x)
    browser.find_element_by_id("solve").click()

finally:
    time.sleep(10)
    browser.quit()
