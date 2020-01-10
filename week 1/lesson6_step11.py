from selenium import webdriver
import time

links = ["http://suninjuly.github.io/registration1.html", "http://suninjuly.github.io/registration2.html"]
for link in links:
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element_by_css_selector(".first:required").send_keys("Ivan")
        browser.find_element_by_css_selector(".second:required").send_keys("Petrov")
        browser.find_element_by_css_selector(".third:required").send_keys("url@gmail")
        browser.find_element_by_css_selector("button.btn").click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        time.sleep(10)
        browser.quit()
