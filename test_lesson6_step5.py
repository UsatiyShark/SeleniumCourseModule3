import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math


@pytest.fixture (scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
@pytest.fixture(scope="function")
def authorize(browser, request):
    wait = WebDriverWait(browser, 15)
    link=request.param
    browser.get(link)
    button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Войти']")))
    button.click()
    google = wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Google']")))
    google.click()
    email = browser.find_element(By.XPATH, "//input[@type='email']")
    time.sleep(4)
    email.send_keys("mygmail@uni-dubna.ru")
    next_button = browser.find_element(By.XPATH, "//span[text()='Далее']")
    next_button.click()
    password = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
    time.sleep(6)
    password.send_keys("mypassword")
    end_of_auth_button = browser.find_element(By.XPATH, "//span[text()='Далее']")
    end_of_auth_button.click()


class TestLessons():
    @pytest.mark.parametrize("authorize", [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
    ], indirect=True)
    def test_first_lesson(self, browser,authorize):
        wait = WebDriverWait(browser, 15)


        answer_element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
        answer=math.log(int(time.time()))
        answer_element.send_keys(answer)
        submit_button=browser.find_element(By.XPATH, "//button[text()='Submit']")
        submit_button.click()
        attempt_result=wait.until(EC.visibility_of_element_located((By.TAG_NAME, "p")))
        text=attempt_result.text
        print(text)

    def test_second_lesson(self, browser, authorize):
        wait = WebDriverWait(browser, 15)

        answer_element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
        answer = math.log(int(time.time()))
        answer_element.send_keys(answer)
        submit_button = browser.find_element(By.XPATH, "//button[text()='Submit']")
        submit_button.click()
        attempt_result=wait.until(EC.visibility_of_element_located((By.TAG_NAME, "p")))
        text=attempt_result.text
        print(text)
        # password = browser.find_element(By.NAME, "password")

    def test_third_lesson(self, browser, authorize):
        wait = WebDriverWait(browser, 15)

        answer_element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
        answer = math.log(int(time.time()))
        answer_element.send_keys(answer)
        submit_button = browser.find_element(By.XPATH, "//button[text()='Submit']")
        submit_button.click()
        attempt_result=wait.until(EC.visibility_of_element_located((By.TAG_NAME, "p")))
        text=attempt_result.text
        print(text)

    def test_fourth_lesson(self, browser, authorize):
        wait = WebDriverWait(browser, 15)

        answer_element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
        answer = math.log(int(time.time()))
        answer_element.send_keys(answer)
        submit_button = browser.find_element(By.XPATH, "//button[text()='Submit']")
        submit_button.click()
        attempt_result=wait.until(EC.visibility_of_element_located((By.TAG_NAME, "p")))
        text=attempt_result.text
        print(text)

    def test_fifth_lesson(self, browser, authorize):
        wait = WebDriverWait(browser, 15)

        answer_element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
        answer = math.log(int(time.time()))
        answer_element.send_keys(answer)
        submit_button = browser.find_element(By.XPATH, "//button[text()='Submit']")
        submit_button.click()
        attempt_result=wait.until(EC.visibility_of_element_located((By.TAG_NAME, "p")))
        text=attempt_result.text
        print(text)

    def test_sixth_lesson(self, browser, authorize):
        wait = WebDriverWait(browser, 15)

        answer_element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
        answer = math.log(int(time.time()))
        answer_element.send_keys(answer)
        submit_button = browser.find_element(By.XPATH, "//button[text()='Submit']")
        submit_button.click()
        attempt_result=wait.until(EC.visibility_of_element_located((By.TAG_NAME, "p")))
        text=attempt_result.text
        print(text)

    def test_seventh_lesson(self, browser, authorize):
        wait = WebDriverWait(browser, 15)

        answer_element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
        answer = math.log(int(time.time()))
        answer_element.send_keys(answer)
        submit_button = browser.find_element(By.XPATH, "//button[text()='Submit']")
        submit_button.click()
        attempt_result = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "p")))
        text = attempt_result.text
        print(text)

    def test_eights_lesson(self, browser, authorize):
        wait = WebDriverWait(browser, 15)

        answer_element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
        answer = math.log(int(time.time()))
        answer_element.send_keys(answer)
        submit_button = browser.find_element(By.XPATH, "//button[text()='Submit']")
        submit_button.click()
        attempt_result=wait.until(EC.visibility_of_element_located((By.TAG_NAME, "p")))
        text=attempt_result.text
        print(text)





