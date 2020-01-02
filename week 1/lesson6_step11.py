from selenium import webdriver
import time

links = ["http://suninjuly.github.io/registration1.html", "http://suninjuly.github.io/registration2.html"]
for link in links:
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector(".first:required").send_keys("Ivan")
        browser.find_element_by_css_selector(".second:required").send_keys("Petrov")
        browser.find_element_by_css_selector(".third:required").send_keys("url@gmail")
        # Отправляем заполненную форму
        browser.find_element_by_css_selector("button.btn").click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

        # пустая строка ;3
