import random
import string
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators
from data import Urls, TestData

def generate_random_email():
    """Генерация случайного email для тестов регистрации"""
    random_string = ''.join(random.choices(string.ascii_lowercase, k=7))
    return f"alexandr_{random_string}@yandex.ru"

def generate_random_password(length=6):
    """Генерация случайного пароля заданной длины"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def login_user(driver):
    """Общий хелпер для авторизации, вынесенный из файлов тестов по требованию ревьюера"""
    driver.get(Urls.LOGIN_URL)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TestData.EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TestData.PASSWORD)
    driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.SUCCESS_LOGIN_MARK))
