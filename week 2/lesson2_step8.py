from selenium import webdriver
import os
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Firefox()
    browser.get(link)

    browser.find_element_by_css_selector("input[name='firstname']").send_keys("Ivan")
    browser.find_element_by_tag_name("input[name='lastname']").send_keys("Andrey")
    browser.find_element_by_tag_name("input[name='email']").send_keys("username@step")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'lesson2_step8.txt')  # добавляем к этому пути имя файла 
    browser.find_element_by_id("file").send_keys(file_path)  # нажали кнопку "обзор" и ввели путь нашего файла
    button = browser.find_element_by_tag_name("button").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # пустая строка ;3
