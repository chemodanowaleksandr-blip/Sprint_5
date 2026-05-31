import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators, ForgotPasswordPageLocators

# Актуальный домен стенда
base_host = "stellarburgers.education-services.ru"

class TestLogin:
    # Учетные данные для входа (мы берем постоянные, чтобы не регистрировать каждый раз заново)
    EMAIL = "alexandr_test_burgers@yandex.ru"
    PASSWORD = "password123"

    def login_helper(self, driver):
        """Вспомогательный метод для заполнения полей ввода и нажатия кнопки Войти"""
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(self.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(self.PASSWORD)
        driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()
        
        # Ждем, пока на главной появится кнопка "Оформить заказ", подтверждающая успешный логин
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.SUCCESS_LOGIN_MARK))

    def test_login_from_main_page_button(self, driver):
        """1. Вход по кнопке 'Войти в аккаунт' на главной"""
        driver.get(f"https://{base_host}/")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_ACCOUNT_BUTTON))
        driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        
        self.login_helper(driver)
        assert driver.find_element(*LoginPageLocators.SUCCESS_LOGIN_MARK).is_displayed()

    def test_login_from_profile_button(self, driver):
        """2. Вход через кнопку 'Личный кабинет' в шапке"""
        driver.get(f"https://{base_host}/")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON))
        driver.find_element(*MainPageLocators.PERSONAL_CABINET_BUTTON).click()
        
        self.login_helper(driver)
        assert driver.find_element(*LoginPageLocators.SUCCESS_LOGIN_MARK).is_displayed()

    def test_login_from_registration_form(self, driver):
        """3. Вход через ссылку 'Войти' на форме регистрации"""
        driver.get(f"https://{base_host}/register")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(RegisterPageLocators.LOGIN_LINK))
        driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
        
        self.login_helper(driver)
        assert driver.find_element(*LoginPageLocators.SUCCESS_LOGIN_MARK).is_displayed()

    def test_login_from_forgot_password_form(self, driver):
        """4. Вход через ссылку 'Войти' на форме восстановления пароля"""
        driver.get(f"https://{base_host}/forgot-password")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(ForgotPasswordPageLocators.LOGIN_LINK))
        driver.find_element(*ForgotPasswordPageLocators.LOGIN_LINK).click()
        
        self.login_helper(driver)
        assert driver.find_element(*LoginPageLocators.SUCCESS_LOGIN_MARK).is_displayed()
