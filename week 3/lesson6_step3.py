import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()


@pytest.mark.parametrize('link', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_stepik_links(browser, link):
    browser.get(f"https://stepik.org/lesson/{link}/step/1")
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".submit-submission")))
    browser.find_element_by_css_selector(".textarea").send_keys(str(math.log(int(time.time()))))
    browser.find_element_by_css_selector(".submit-submission").click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    assert browser.find_element_by_css_selector(".smart-hints__hint").text == "Correct!", "Wrong"
