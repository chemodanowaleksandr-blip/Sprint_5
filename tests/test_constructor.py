import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators
from helpers import TestData

class TestConstructorAndProfile:

    def login_helper(self, driver):
        """Вспомогательный метод для авторизации перед тестами профиля"""
        driver.get(f"https://{TestData.BASE_HOST}/login")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TestData.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TestData.PASSWORD)
        driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.SUCCESS_LOGIN_MARK))

    def test_go_to_personal_cabinet(self, driver):
        """1. Проверка перехода в личный кабинет"""
        self.login_helper(driver)
        
        cabinet_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON))
        driver.execute_script("arguments[0].click();", cabinet_btn)
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePageLocators.EXIT_BUTTON))
        assert "account" in driver.current_url

    def test_go_from_profile_to_constructor_via_button(self, driver):
        """2. Переход из личного кабинета в конструктор по кнопке 'Конструктор'"""
        self.login_helper(driver)
        
        cabinet_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON))
        driver.execute_script("arguments[0].click();", cabinet_btn)
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePageLocators.EXIT_BUTTON))
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.SUCCESS_LOGIN_MARK))
        assert "account" not in driver.current_url

    def test_go_from_profile_to_constructor_via_logo(self, driver):
        """3. Переход из личного кабинета в конструктор по клику на логотип"""
        self.login_helper(driver)
        
        cabinet_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON))
        driver.execute_script("arguments[0].click();", cabinet_btn)
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePageLocators.EXIT_BUTTON))
        driver.find_element(*MainPageLocators.LOGO_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.SUCCESS_LOGIN_MARK))
        assert "account" not in driver.current_url

    def test_logout_from_profile(self, driver):
        """4. Выход из аккаунта по кнопке 'Выход' в личном кабинете"""
        self.login_helper(driver)
        
        cabinet_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON))
        driver.execute_script("arguments[0].click();", cabinet_btn)
        
        exit_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePageLocators.EXIT_BUTTON))
        driver.execute_script("arguments[0].click();", exit_btn)
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.ENTER_BUTTON))
        assert "login" in driver.current_url

    def test_constructor_tabs_sauces(self, driver):
        """5.1 Проверка перехода на вкладку 'Соусы'"""
        driver.get(f"https://{TestData.BASE_HOST}/")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.LOGIN_ACCOUNT_BUTTON))
        
        tab_element = driver.find_element(*MainPageLocators.SAUCES_TAB)
        driver.execute_script("arguments[0].click();", tab_element)
        
        WebDriverWait(driver, 5).until(lambda d: "tab_tab_type_current" in tab_element.get_attribute("class"))
        assert "tab_tab_type_current" in tab_element.get_attribute("class")

    def test_constructor_tabs_fillings(self, driver):
        """5.2 Проверка перехода на вкладку 'Начинки'"""
        driver.get(f"https://{TestData.BASE_HOST}/")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.LOGIN_ACCOUNT_BUTTON))
        
        tab_element = driver.find_element(*MainPageLocators.FILLINGS_TAB)
        driver.execute_script("arguments[0].click();", tab_element)
        
        WebDriverWait(driver, 5).until(lambda d: "tab_tab_type_current" in tab_element.get_attribute("class"))
        assert "tab_tab_type_current" in tab_element.get_attribute("class")

    def test_constructor_tabs_buns(self, driver):
        """5.3 Проверка перехода на вкладку 'Булки'"""
        driver.get(f"https://{TestData.BASE_HOST}/")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.LOGIN_ACCOUNT_BUTTON))
        
        sauce_element = driver.find_element(*MainPageLocators.SAUCES_TAB)
        driver.execute_script("arguments[0].click();", sauce_element)
        WebDriverWait(driver, 5).until(lambda d: "tab_tab_type_current" in sauce_element.get_attribute("class"))
        
        bun_element = driver.find_element(*MainPageLocators.BUNS_TAB)
        driver.execute_script("arguments[0].click();", bun_element)
        
        WebDriverWait(driver, 5).until(lambda d: "tab_tab_type_current" in bun_element.get_attribute("class"))
        assert "tab_tab_type_current" in bun_element.get_attribute("class")
