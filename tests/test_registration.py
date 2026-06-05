import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegisterPageLocators, LoginPageLocators
from helpers import generate_random_email, generate_random_password
from data import Urls

class TestRegistration:

    def test_successful_registration(self, driver):
        """1. Успешная регистрация пользователя с валидными данными"""
        driver.get(Urls.REGISTER_URL)
        email = generate_random_email()
        password = generate_random_password(6)
    
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT))
    
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Александр")
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    
        WebDriverWait(driver, 15).until(EC.url_to_be(Urls.LOGIN_URL))
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.ENTER_BUTTON))

    def test_registration_password_error(self, driver):
        """2. Ошибка при регистрации пользователя с некорректным (коротким) паролем"""
        driver.get(Urls.REGISTER_URL)
        email = generate_random_email()
        incorrect_password = generate_random_password(5)
        
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT))
        
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Александр")
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(incorrect_password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        
        # Исправлено: Ожидание маркера ошибки встроено непосредственно в ассерт
        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR_MESSAGE)
        ).is_displayed()
