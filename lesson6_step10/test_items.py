import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def test_add_to_cart_button(browser, language):
    # Переход на страницу (замените на нужный URL)
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(3)
    # Выбор языка из селекта
    language_select = browser.find_element(By.NAME, 'language')
    language_select.click()

    # Выбор нужного языка
    language_option = browser.find_element(By.XPATH, f"//option[@value='{language}']")
    language_option.click()

    time.sleep(2)
    browser.execute_script("arguments[0].blur();", language_select)


    # Нажатие кнопки подтверждения выбора языка
    wait = WebDriverWait(browser, 10)
    submit_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn') and contains(@class, 'btn-default')]")))

    try:
        submit_button.click()
    except Exception as e:
        print(f"Ошибка при нажатии на кнопку: {e}")

    time.sleep(5)

    # Ожидание появления кнопки "Добавить в корзину"
    add_to_cart_button = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'btn') and contains(@class, 'btn-primary')]")))

    # Проверка наличия кнопки "Добавить в корзину"
    assert add_to_cart_button.is_displayed(), f"Кнопка 'Добавить в корзину' не найдена для языка: {language}"