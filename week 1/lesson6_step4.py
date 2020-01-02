from selenium import webdriver
import time
import math

# https://habr.com/ru/post/250975/   Пример работы этих методов...

link = "http://suninjuly.github.io/find_link_text"

try:
    # browser = webdriver.Chrome()
    browser = webdriver.Firefox()
    browser.get(link)
    text = str(math.ceil(math.pow(math.pi, math.e) * 10000))  # зашифрованная ссылка
    link = browser.find_element_by_link_text(text)
    link.click()

    value1, value2, value3, value4 = 'input', 'last_name', 'city', 'country'
    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
