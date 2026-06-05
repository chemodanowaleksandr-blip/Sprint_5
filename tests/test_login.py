import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators, ForgotPasswordPageLocators
from data import Urls, TestData

class TestLogin:

    def test_login_from_main_page_button(self, driver):
        """1. Вход по кнопке 'Войти в аккаунт' на главной странице"""
        driver.get(Urls.BASE_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.LOGIN_ACCOUNT_BUTTON))
        driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TestData.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TestData.PASSWORD)
        driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.SUCCESS_LOGIN_MARK))

    def test_login_from_profile_button(self, driver):
        """2. Вход через кнопку 'Личный Кабинет' в шапке сайта"""
        driver.get(Urls.BASE_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_CABINET_BUTTON))
        driver.find_element(*MainPageLocators.PERSONAL_CABINET_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TestData.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TestData.PASSWORD)
        driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.SUCCESS_LOGIN_MARK))

    def test_login_from_registration_form(self, driver):
        """3. Вход через ссылку 'Войти' на странице регистрации"""
        driver.get(Urls.REGISTER_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegisterPageLocators.LOGIN_LINK))
        driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TestData.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TestData.PASSWORD)
        driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.SUCCESS_LOGIN_MARK))

    def test_login_from_forgot_password_form(self, driver):
        """4. Вход через ссылку 'Войти' на странице восстановления пароля"""
        driver.get(Urls.FORGOT_PASSWORD_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ForgotPasswordPageLocators.LOGIN_LINK))
        driver.find_element(*ForgotPasswordPageLocators.LOGIN_LINK).click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TestData.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TestData.PASSWORD)
        driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.SUCCESS_LOGIN_MARK))
