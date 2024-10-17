import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_registration1(browser):
    link = "https://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CLASS_NAME, "first")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.CLASS_NAME, "second")
    input2.send_keys("Ivanov")

    input3 = browser.find_element(By.CLASS_NAME, "third")
    input3.send_keys("Ivan@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # Проверяем, что смогли зарегистрироваться
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert welcome_text == "Congratulations! You have successfully registered!"

def test_registration2(browser):
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CLASS_NAME, "first")
    input1.send_keys("Ivan")

    input2 = browser.find_element((By.XPATH, "//input[@class='second' and @required]"))
    input2.send_keys("Ivan@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # Проверяем, что смогли зарегистрироваться
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert welcome_text == "Congratulations! You have successfully registered!"
